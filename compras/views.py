from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import AnonymousUser

from .models import Compra


class CompraListView(ListView):
    model = Compra
    template_name = 'compra_lista.html'
    login_url = 'login'

    def get_queryset(self):
        if self.request.user != AnonymousUser():
            usuario = self.request.user
            queryset = Compra.objects.filter(revendedor=usuario)
            return queryset
        else:
            raise PermissionDenied

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
