from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	# Painel de administrador
    path('gerenciador', admin.site.urls),

    # Gerenciador de usuarios
    path('contas/', include('django.contrib.auth.urls')),

    # Apps
    path('contas/', include('usuarios.urls')), 
    path('', include('paginas.urls')), 
]
