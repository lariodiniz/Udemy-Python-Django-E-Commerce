#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.conf import settings

from accounts.models import User

from model_mommy import mommy

class RegisterViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('accounts:register')  

    def test_register_ok(self):
        data = {'username': 'test', 
            'password1':'teste123', 
            'password2':'teste123',
            'email': 'test@test.com'}
        response = self.client.post(self.url, data)  
        index_url = reverse('index')        
        self.assertRedirects(response, index_url)
        self.assertEquals(User.objects.count(), 1)
        
    def test_register_erro(self):
        data = {'username': 'lario', 'password1':'teste123', 'password2':'teste123'}
        response = self.client.post(self.url, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')


class UpdateUserViewTestCase(TestCase): 

    def setUp(self):
        self.client = Client()
        self.url = reverse('accounts:update_user')  
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('123')
        self.user.save()
    
    def tearDown(self):
        self.user.delete()

    def test_update_user_ok(self):
        data = {'name': 'teste', 'email':'teste@teste.com'}
        response = self.client.get(self.url)      
        self.assertEquals(response.status_code, 302)
        self.client.login(username=self.user.username, password='123')
        response = self.client.post(self.url, data)  
        accounts_index_url = reverse('accounts:index')
        self.assertRedirects(response, accounts_index_url)
        #user = User.objects.get(username =self.user.username)
        self.user.refresh_from_db()
        self.assertEquals(self.user.email, 'teste@teste.com')

    def test_update_user_error(self):
        data = {}
        self.client.login(username=self.user.username, password='123')
        response = self.client.post(self.url, data)  
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')      


class UpdatePasswordViewTestCase(TestCase): 

    def setUp(self):
        self.client = Client()
        self.url = reverse('accounts:update_password')  
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('123')
        self.user.save()
    
    def tearDown(self):
        self.user.delete()

    def test_update_password_ok(self):
        data = {'old_password': '123', 'new_password1':'teste123', 'new_password2':'teste123'}
        self.client.login(username=self.user.username, password='123')
        response = self.client.post(self.url, data)  
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('teste123'))

