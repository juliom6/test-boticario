# Generated by Django 3.0.3 on 2020-02-21 13:17

import cpffield.cpffield
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_auto_20200219_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='revendedor',
            name='alt_cpf',
            field=cpffield.cpffield.CPFField(default='', max_length=14, verbose_name='CPF'),
        ),
    ]
