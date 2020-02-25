from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
	# Painel de administrador
    path('gerenciador/', admin.site.urls),

    # Gerenciador de usuarios
    path('contas/', include('django.contrib.auth.urls')),

    # Apps
    path('contas/', include('usuarios.urls')), 
    path('compras/', include('compras.urls')), 
    path('', include('paginas.urls')),

    # Tokens JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

admin.site.site_header = 'O Boticário || Painel de Administração'
admin.site.site_title = 'O Boticário'