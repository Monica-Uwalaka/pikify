from django.contrib.auth.models import AnonymousUser, User
from django.contrib.auth import authenticate
from django.test import TestCase

from rest_framework.test import APIRequestFactory

from pikify.views import Home

#make sure anonymous user does not access home
class HomeViewTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user_test = self.user_test = User.objects.create(first_name='firstname_test', last_name='lastname_test', username = 'username_test', email = 'user_test@gmail.com', password = 'password_test')

    def test_get(self):
        # Create an instance of a GET request.
        request = self.factory.get('home')

        #simulate a logged in user
        request.user = self.user_test
        
        #make sure the user is authenticated
        response = Home.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(request.user.is_authenticated)
        


