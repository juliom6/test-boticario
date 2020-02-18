from django.urls import path

from .views import PaginaCadastroView

urlpatterns = [
    path('cadastro/', PaginaCadastroView.as_view(), name='cadastro'),
]