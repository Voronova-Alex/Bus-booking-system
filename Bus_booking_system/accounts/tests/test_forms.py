from django.test import TestCase
from accounts.forms import SignUpForm


class SignUpFormTest(TestCase):

    def test_form_right(self):
        form_data = {
            'username': 'test',
            'first_name': 'Test',
            'last_name': 'Test',
            'email': 'test@test.com',
            'password1': 'test_TEST_1',
            'password2': 'test_TEST_1'
        }

        form = SignUpForm(form_data)
        self.assertTrue(form.is_valid())

    def test_user_form_wrong(self):
        form_data = {
            'username': 'test',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com',
            'password1': 'test_TEST',
            'password2': 'test_TEST_1'
        }
        form = SignUpForm(form_data)
        self.assertFalse(form.is_valid())
