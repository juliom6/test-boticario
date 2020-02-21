from django.views.generic import ListView

from .models import Compra


class CompraListView(ListView):
	model = Compra
	template_name = 'compra_list.html'