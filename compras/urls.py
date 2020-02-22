from django.urls import path

from .views import (
	CompraListView,
	CompraCreateView,
	CompraDetailView,
	CompraUpdateView,
	CompraDeleteView,
	)

urlpatterns = [
	path('', CompraListView.as_view(), name='compra_lista'),
	path('novo/', CompraCreateView.as_view(), name='compra_novo'),
	path('<int:pk>/editar/', CompraUpdateView.as_view(), name='compra_editar'),
	path('<int:pk>/', CompraDetailView.as_view(), name='compra_detalhe'),
	path('<int:pk>/apagar/', CompraDeleteView.as_view(), name='compra_apagar'),
]