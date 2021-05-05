"""
serializers.py defines Serializers that help convert our Django models to JSON and vice-versa.
We have one Serializer for each of our models, and we specify exactly what fields should be serialized.
"""

from django.contrib.auth.models import User, Group
from .models import PikifyUser, Image
from rest_framework import serializers

class PikifyUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PikifyUser
        fields = ['id', 'firstName', 'lastName', 'createdAt', 'displayName', 'password', 'profileImageUrl']

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image 
        fields = ['id', 'user', 'url', 'private']
