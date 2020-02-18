from django.urls import path

from .views import PaginaInicioView


urlpatterns = [
    path('', PaginaInicioView.as_view(), name='inicio'),
]