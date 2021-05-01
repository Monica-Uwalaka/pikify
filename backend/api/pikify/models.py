import uuid
from django.db import models


# Create your models here.

# Represents a user on Pikify
class PikifyUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    displayName = models.TextField()  

# Represents an image on Pikify
class Image(models.Model):
    pass
