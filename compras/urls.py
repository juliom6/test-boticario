from django.urls import path

from .views import CompraListView

urlpatterns = [
	path('', CompraListView.as_view(), name='compra_list')
]