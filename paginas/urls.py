from django.urls import path

from .views import PaginaInicioView, tempoView


urlpatterns = [
    path('', PaginaInicioView.as_view(), name='inicio'),
    path('tempo', tempoView, name='tempo'),
]