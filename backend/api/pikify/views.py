from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout

from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from .models import PikifyUser, Image
from .serializers import PikifyUserSerializer, ImageSerializer


class Index(APIView):
    """
    GET: view index page
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request, format = None):
        #render sign up form
        return render(request, 'index.html')
    

class SignUp(APIView):
    """
    GET: View sign up page 
    POST: Sign up new user 
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'signup.html'

    def get(self, request, format = None):
        #render sign up form
        return render(request, 'signup.html')

    def post(self, request, format = None):
        #create user 
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(first_name = first_name, last_name = last_name, username = username, email = email, password = password)
        user.save()
        return redirect('home')
      

class SignIn(APIView):
    """
    GET: View sign up page 
    POST: Sign up new user 
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'signin.html'

    def get(self, request, format = None):
        #render sign in form
        return render(request, 'signin.html')

    def post(self, request, format = None):
        #sign in user
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
        
        else:
            # Return an 'invalid login' error message.
            return redirect('sign-in')

class SignOut(APIView):
    """
    GET: View sign up page 
    POST: Sign up new user 
    """

    def get(self, request, format = None):
        #render sign in form
        logout(request)
        return redirect('index')

class Home(APIView):
    """
    GET: View home page
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self, request, format = None):
        #render sign in form
        return render(request, 'home.html')

def myRepo(request):
    return HttpResponse("You are in your repo")


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






















# class PikifyUserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = PikifyUser.objects.all()
#     serializer_class = PikifyUserSerializer

#     # Using lookup_field as search param
#     # https://stackoverflow.com/questions/56431755/django-rest-framework-urls-without-pk
#     lookup_field = 'id'

#     def retrieve(self, request, id):
#         try: 
#             pikify_user = PikifyUser.objects.get(id=id)
#             serializer = PikifyUserSerializer(pikify_user)

#         except(PikifyUser.DoesNotExist):
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         return Response(serializer.data)
