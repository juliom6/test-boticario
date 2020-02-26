# Teste Boticario

Source code of website http://juliom6.pythonanywhere.com/


Desenvolvido usando Django

Para instalar localmente

```console
git clone https://github.com/juliom6/test-boticario.git
cd test-boticario
python -m pip install pipenv
pipenv install
pipenv shell
```

Para migrar o banco de dados (testado com postgresql e sqlite):

```console
python manage.py migrate
``` 

Para criar um superusuario (usuarios normais podem ser criados desde o app):

```console
python manage.py createsuperuser
```

Para rodar o servidor em desenvolvimento:

```console
python manage.py runserver
```

Para rodar o servidor em produção:

```console
waitress-serve --port=80 cashback_project.wsgi:application
```

Para rodar os testes:

```console
python manage.py test
```

Have fun!