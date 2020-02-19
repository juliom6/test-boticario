from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model

from .views import PaginaInicioView


class PaginaInicioTests(SimpleTestCase):

    def setUp(self):
        url = reverse('inicio')
        self.response = self.client.get(url)

    def test_pagina_inicio_codigo_status(self):
        self.assertEqual(self.response.status_code, 200)

    def test_view_url_pelo_nome(self):
        response = self.client.get(reverse('cadastro'))
        self.assertEqual(response.status_code, 200)

    def test_pagina_inicio_template(self):
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(self.response, 'inicio.html')

    def test_pagina_inicio_contem_html(self):
        self.assertContains(self.response, 'em-vindo')

    def test_pagina_inicio_nao_contem_html(self):
        self.assertNotContains(
            self.response, 'Texto nao presente no codigo')

    def test_pagina_inicio_url_resolve_paginainicioview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            PaginaInicioView.as_view().__name__
        )


class PaginaCadastroTests(TestCase):

    usuario = 'usuario'
    email = 'usuario@gmail.com'

    def test_pagina_cadastro_status_code(self):
        response = self.client.get('/contas/cadastro/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_pelo_nome(self):
        response = self.client.get(reverse('cadastro'))
        self.assertEqual(response.status_code, 200)

    def test_view_usa_template_correcta(self):
        response = self.client.get(reverse('cadastro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cadastro.html')

    def test_formulario_cadastro(self):
        novo_usuario = get_user_model().objects.create_user(self.usuario, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.usuario)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)