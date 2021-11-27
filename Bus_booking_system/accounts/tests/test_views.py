from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from accounts.tokens import account_activation_token


class BaseTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.singup_url = reverse('signup')
        self.login_url = reverse('login')
        self.user = {
            'username': 'test',
            'first_name': 'Test',
            'last_name': 'Test',
            'email': 'test@test.com',
            'password1': 'test_TEST_1',
            'password2': 'test_TEST_1'
        }

    def test_can_view_page_correctly(self):
        response = self.client.get(self.singup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_can_sighup_user(self):
        response = self.client.post(self.singup_url, data=self.user)
        self.assertEqual(response.status_code, 302)


class LoginTest(BaseTest):
    def test_can_access_page(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_success(self):
        response = self.client.post(self.login_url, self.user)
        self.assertEqual(response.status_code, 200)


class ActivateAccountTest(BaseTest):
    def test_user_activate_account_success(self):
        user = User.objects.create_user('test', 'test@test.com')
        user.set_password('test_TEST_1')
        user.is_active = False
        user.save()
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = account_activation_token.make_token(user)
        response = self.client.get(reverse('activate', kwargs={'uidb64': uid, 'token': token}))
        user = User.objects.get(email='test@test.com')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(user.is_active)
