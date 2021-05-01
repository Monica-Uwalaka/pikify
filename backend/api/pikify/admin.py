"""
admin.py registers models so that they can be created/modified/deleted from the admin page.
"""

from django.contrib import admin
from .models import PikifyUser

# Register your models here.
admin.site.register(PikifyUser)
