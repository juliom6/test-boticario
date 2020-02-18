from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve 

from .forms import RevendedorCreationForm 
from .views import PaginaCadastroView


class RevendedorTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='julio',
            email='juliom6@gmail.com',
            password='Unodos34'
        )
        self.assertEqual(user.username, 'julio')
        self.assertEqual(user.email, 'juliom6@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class PaginaCadastroTests(TestCase):

    def setUp(self):
        url = reverse('cadastro')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'cadastro.html')
        self.assertContains(self.response, 'Cadastro')
        self.assertNotContains(
            self.response, 'Texto que nao existe na pagina')

    def test_signup_form(self): 
        form = self.response.context.get('form')
        self.assertIsInstance(form, RevendedorCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self): 
        view = resolve('/contas/cadastro/')
        self.assertEqual(
            view.func.__name__,
            PaginaCadastroView.as_view().__name__
        )