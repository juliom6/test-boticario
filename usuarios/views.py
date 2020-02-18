from django.urls import reverse_lazy
from django.views import generic

from .forms import RevendedorCreationForm


class PaginaCadastroView(generic.CreateView):
    form_class = RevendedorCreationForm
    success_url = reverse_lazy('login')
    template_name = 'cadastro.html'