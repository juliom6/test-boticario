from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class RevendedorCreationForm(UserCreationForm):

    email = forms.CharField(label='Email')
    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='Sobrenome')

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'cpf')
        fields_required = ['email']


class RevendedorChangeForm(UserChangeForm):

    email = forms.CharField(label='Email')
    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='Sobrenome')

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'last_name', 'last_name', 'cpf')
        fields_required = ['email']
