from django.urls import path

from .views import PaginaInicioView, tempoView, contatoView


urlpatterns = [
    path('', PaginaInicioView.as_view(), name='inicio'),
    path('tempo', tempoView, name='tempo'),
    path('contato', contatoView, name='contato'),
]