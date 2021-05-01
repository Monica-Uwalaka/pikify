from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from .models import PikifyUser
from .serializers import PikifyUserSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the pikify index.")

class PikifyUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PikifyUser.objects.all()
    serializer_class = PikifyUserSerializer

    # Using lookup_field as search param
    # https://stackoverflow.com/questions/56431755/django-rest-framework-urls-without-pk
    lookup_field = 'id'

    def retrieve(self, request, id):
        try: 
            pikify_user = PikifyUser.objects.get(id=id)
            serializer = PikifyUserSerializer(pikify_user)

        except(PikifyUser.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.data)
