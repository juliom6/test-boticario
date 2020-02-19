from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import PaginaInicioView


class PaginaInicioTests(SimpleTestCase):

    def setUp(self):
        url = reverse('inicio')
        self.response = self.client.get(url)

    def test_pagina_inicio_codigo_status(self):
        self.assertEqual(self.response.status_code, 200)

    def test_pagina_inicio_template(self):
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