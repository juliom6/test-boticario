from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from cpffield import cpffield

class Revendedor(AbstractUser):
    username = models.CharField(_('username'), max_length=50, unique=True)
    email = models.EmailField(_('email address'), blank=True, unique=True)
    cpf = cpffield.CPFField('CPF', max_length=11, default='', unique=True, blank=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'cpf']
