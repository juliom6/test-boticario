from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Compra


class CompraListView(ListView):
    model = Compra
    template_name = 'compra_lista.html'


class CompraCreateView(CreateView):
    model = Compra
    template_name = 'compra_novo.html'
    fields = ('codigo', 'valor', 'revendedor')

class CompraDetailView(DetailView):
    model = Compra
    template_name = 'compra_detalhe.html'

class CompraUpdateView(UpdateView):
    model = Compra
    fields = ('codigo', 'valor')
    template_name = 'compra_editar.html'

class CompraDeleteView(DeleteView):
    model = Compra
    template_name = 'compra_apagar.html'
    success_url = reverse_lazy('compra_lista')
