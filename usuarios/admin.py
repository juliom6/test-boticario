from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import RevendedorCreationForm, RevendedorChangeForm

Revendedor = get_user_model()


class RevendedorAdmin(UserAdmin):
    add_form = RevendedorCreationForm
    form = RevendedorChangeForm
    model = Revendedor
    list_display = ['email', 'username',]

admin.site.register(Revendedor, RevendedorAdmin)