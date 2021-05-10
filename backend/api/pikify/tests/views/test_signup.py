from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase

from rest_framework.test import APIRequestFactory

from pikify.views import SignUp
from pikify.forms import UserSignUpForm


class SignUpViewTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user_test = self.user_test = User.objects.create(first_name='firstname_test', last_name='lastname_test', username = 'username_test', email = 'user_test@gmail.com', password = 'password_test')

    def test_get(self):
        # Create an instance of a GET request.
        request = self.factory.get('sign-up')

        #simulate a logged in user
        request.user = self.user_test

        #simulate an AnnonymousUser Instance
        request.user = AnonymousUser()

        response = SignUp.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        # Create an instance of form
        print(self.user_test)
        form_data = {'first_name':'firstname_test', 'last_name':'lastname_test', 'username':'username_test', 'email':'user_test@gmail.com', 'password': 'password_test'}
        form = UserSignUpForm(form_data)
        context = {
        'title': 'Sign up',
        'form': form
        }

        # Create an instance of a POST request.
        request = self.factory.post('sign-up', context)
        
        #simulate a logged in user
        request.user = self.user_test

        #simulate an AnnonymousUser Instance
        request.user = AnonymousUser()

        response = SignUp.as_view()(request)
        self.assertEqual(response.status_code, 200)


