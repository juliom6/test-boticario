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

Para migrar o banco de dados:

```console
python manage.py migrate
``` 

Para criar um usuario:

```console
python manage.py createsuperuser
```

Para rodar o servidor localmente:

```console
python manage.py runserver
```

Para rodar os testes:

```console
pytest cashback
```

Para instalar no docker e rodar

```console
docker-compose docker-compose.yml up
```

and add to your .env

```console
DATABASE_URL=postgres://boticario:boticario@localhost:5432/cashback
```

Have fun!