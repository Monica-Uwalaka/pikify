from django.test import TestCase
from pikify.models import Image
from django.contrib.auth.models import User


class ImageModelTest(TestCase):
    """Test for creating an Image"""

    def setUp(self):
        # Set up non-modified objects used by all test methods
        self.user_test = User.objects.create(first_name='firstname_test', last_name='lastname_test', username = 'username_test', email = 'user_test@gmail.com', password = 'password_test')
        self.image_test = Image.objects.create(user = self.user_test, url = "url_test", private = True)


    def test_create_Image(self):
        self.assertTrue(self.image_test.id)
        self.assertTrue(self.image_test.user)
        self.assertTrue(self.image_test.private)

        self.assertEqual(self.image_test.url, 'url_test')
        self.assertEqual(self.image_test.user_id, self.user_test.id)



        