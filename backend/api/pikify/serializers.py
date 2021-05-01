"""
serializers.py defines Serializers that help convert our Django models to JSON and vice-versa.
We have one Serializer for each of our models, and we specify exactly what fields should be serialized.
"""

from django.contrib.auth.models import User, Group
from .models import PikifyUser
from rest_framework import serializers

class PikifyUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PikifyUser
        fields = ['id', 'displayName']
