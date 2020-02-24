from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework.permissions import IsAuthenticated

from django.utils.functional import SimpleLazyObject
from django.contrib.auth.middleware import get_user
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
        print(type(self.request.user))
        queryset = Compra.objects.filter(revendedor=usuario)
        return queryset

class CompraCreateView(LoginRequiredMixin, CreateView):
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
    model = Compra
    template_name = 'compra_detalhe.html'
    login_url = 'login'

class CompraUpdateView(UpdateView):
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
    model = Compra
    template_name = 'compra_apagar.html'
    success_url = reverse_lazy('compra_lista')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        compra = self.get_object()
        if compra.revendedor != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
