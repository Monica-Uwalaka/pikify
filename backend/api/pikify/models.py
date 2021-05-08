from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

# Represents a user on Pikify
class PikifyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # https://www.ordinarycoders.com/django-custom-user-profile

    def __str__(self):
        return f'{self.user.username} PikifyUser'
        
# Represents an image on Pikify
class Image(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = '')
    url = models.TextField(default = '')
    private = models.BooleanField(default = '')
