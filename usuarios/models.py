from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class Revendedor(AbstractUser):
	nome_completo = models.CharField(max_length=60, default='')
	# cpf = models.CharField(max_length=14, default='',validators=[RegexValidator(regex='^\d{3}\.\d{3}\.\d{3}\-\d{2}$', message='Como minimo 11 digitos', code='nomatch')])
	cpf = models.CharField(max_length=11, default='', validators=[RegexValidator(regex='^\d{11}$', message='Escreva so os 11 digitos')])
