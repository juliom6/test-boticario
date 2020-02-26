from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework.permissions import IsAuthenticated
from django.utils.functional import SimpleLazyObject
from django.contrib.auth.middleware import get_user
from django.views.generic import TemplateView
import requests
from django.contrib.auth import get_user_model
# from django.views.decorators.csrf import csrf_protect
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Compra

class CompraListView(LoginRequiredMixin, ListView):
    permission_classes = (IsAuthenticated,)
    model = Compra
    template_name = 'compra_lista.html'
    login_url = 'login'

    # @staticmethod
    # def get_jwt_user(request):
    #     user = get_user(request)
    #     if user.is_authenticated:
    #         return user
    #     jwt_authentication = JSONWebTokenAuthentication()
    #     if jwt_authentication.get_jwt_value(request):
    #         user, jwt = jwt_authentication.authenticate(request)
    #     return user

    def get_queryset(self):
        # print(get_user(SimpleLazyObject(lambda:self.__class__.get_jwt_user(request))))
        usuario = self.request.user
        queryset = Compra.objects.filter(revendedor=usuario)
        return queryset

class CompraCreateView(LoginRequiredMixin, CreateView):
    permission_classes = (IsAuthenticated,)
    model = Compra
    template_name = 'compra_novo.html'
    fields = ('codigo', 'valor')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.revendedor = self.request.user
        if self.request.user.cpf == '15350946056':
            form.instance.status = 'A'
        else:
            form.instance.status = 'E'
        return super().form_valid(form)

class CompraDetailView(DetailView):
    permission_classes = (IsAuthenticated,)
    model = Compra
    template_name = 'compra_detalhe.html'
    login_url = 'login'

class CompraUpdateView(UpdateView):
    permission_classes = (IsAuthenticated,)
    model = Compra
    fields = ('codigo', 'valor')
    template_name = 'compra_editar.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        compra = self.get_object()
        if compra.revendedor != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class CompraDeleteView(DeleteView):
    permission_classes = (IsAuthenticated,)
    model = Compra
    template_name = 'compra_apagar.html'
    success_url = reverse_lazy('compra_lista')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        compra = self.get_object()
        if compra.revendedor != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class CashbackView(LoginRequiredMixin, TemplateView):
    permission_classes = (IsAuthenticated,)
    login_url = 'login'
    template_name = 'cashback.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CashbackView, self).get_context_data(*args, **kwargs)

        # if self.request.user.is_authenticated:
        usuario = get_user_model().objects.filter(username__exact=self.request.user)[0]
        payload = {'cpf': usuario.cpf}
        header = {'token' : 'ZXPURQOARHiMc6Y0flhRC1LVlZQVFRnm'}

        try:
            r = requests.get('https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback', params=payload, headers=header)
        except ConnectionError:
            return HttpResponse(status=504) # Gateway Timeout
        else:
            json = r.json()
            if json['statusCode'] == 200:
                context['valor'] = json['body']['credit']

        return context