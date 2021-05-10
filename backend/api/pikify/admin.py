"""
admin.py registers models so that they can be created/modified/deleted from the admin page.
"""

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import PikifyUser

# Register your models here.
admin.site.register(PikifyUser)

#To add pikify user's field to the user page in the admin, define an InlineModelAdmin

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class PikifyUserInLine(admin.StackedInline):
    model = PikifyUser
    can_delete = False
    verbose_name_plural = 'pikifyuser'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (PikifyUserInLine,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)