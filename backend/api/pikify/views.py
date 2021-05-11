from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserSignUpForm, searchImageForm

from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import generics
from rest_framework.parsers import JSONParser

from .models import PikifyUser, Image
from .serializers import PikifyUserSerializer, ImageSerializer
import json

from pexels_api import API

PEXELS_API_KEY = '563492ad6f917000010000015fed1bf3240b45b783e929fb372a40eb'
api = API(PEXELS_API_KEY)

class Index(APIView):
    """
    GET: view index page
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pikify/index.html'

    def get(self, request, format = None):
        #render sign up form
        return render(request, 'pikify/index.html')
    
class SignUp(APIView):
    """
    GET: View sign up page 
    POST: Sign up new user 
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pikify/signup.html'

    def get(self, request, format = None):
        #render sign up form
        form = UserSignUpForm()
        context = {
        'title': 'Sign up',
        'form': form
        }
        return render(request, 'pikify/signup.html', context)

    def post(self, request, format = None):
        #validate sign up form
        #create user 
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created {username} ! You can now sign in')
            return redirect('sign-in')
        else:
            form = UserSignUpForm(request.POST)
            context = {
            'title': 'Sign up',
            'form': form
            }
            return render(request, 'pikify/signup.html', context)

class Home(APIView):
    """
    GET: View home page
    POST: View search results 
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pikify/home.html'

    def get(self, request, format = None):
        return render(request, 'pikify/home.html')

    def post(self, request, format = None):
        form = searchImageForm(request.POST)

        #validate search form
        if form.is_valid():
            searched = form.cleaned_data.get('searched')

            #do the request here
            api.search(searched, page=1, results_per_page=30)
            photos = api.get_entries()

            photo_urls = []
            for photo in photos:
                photo_urls.append(photo.medium)

            context = {
                'searched':searched,
                'urls': photo_urls
            }
            return render(request, 'pikify/search.html', context)

        else:
            searchImageForm(request.POST)
            context = {
                'form': form
            }
            return render(request, 'pikify/home.html', context)
       

class Profile(APIView):
    """
    GET: View signed in user profile
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pikify/home.html'

    #@method_decorator(login_required)
    def get(self, request, format = None):
        #render sign in form
        return render(request, 'pikify/profile.html')


class Search(APIView):

    serializer_class = ImageSerializer
    template_name = 'pikify/myrepo.html'
    parser_classes = [JSONParser]
    

    def get (self, request):
        return render(request, 'pikify/search.html')

    
    def post(self, request, format = None):
        #save the images to the database 
        
        data = request.data
        
        for url in data:
            Image.objects.create(user = request.user, url = url, private = True)

        return HttpResponse({'received data': request.data})



class MyRepo(APIView):

    serializer_class = ImageSerializer
    template_name = 'pikify/myrepo.html'
    

    def get(self, request, format = None):
        images = Image.objects.filter(user = request.user).values('url')
        print("here")
        print(images)
        context = {
        'images' : images
        }
        return render(request, 'pikify/myrepo.html', context)

    def post(self, request, format = None):
        #delete the images from database 
        
        data = request.data
        
        for url in data:
            Image.objects.get(user = request.user, url = url).delete()

        return render(request, 'pikify/myrepo.html')




class UserList(APIView):
    """
    List all users, or create a new user.
    """
    def get(self, request, format=None):
        users = PikifyUser.objects.all()
        serializer = PikifyUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PikifyUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, id):
        try:
            return PikifyUser.objects.get(id=id)
        except PikifyUser.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        user = self.get_object(id)
        serializer = PikifyUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        user = self.get_object(id)
        serializer = PikifyUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        user = self.get_object(id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
