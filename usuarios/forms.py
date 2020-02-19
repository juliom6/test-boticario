from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RevendedorCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'nome_completo', 'cpf')


class RevendedorChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'email',  'nome_completo', 'cpf')