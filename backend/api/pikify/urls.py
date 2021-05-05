"""
urls.py defines all the endpoints of our API service, as defined in the project requirements spec.
It also contains some extra endpoints for our own front-end client to use.
"""
from django.urls import path, include
from . import views

# Debug site/endpoints that DRF helps us implement.
# Routers provide an easy way of automatically determining the URL conf.


urlpatterns = [
  # Paths API endpoints
  #pikify Home page
  path('', views.Index.as_view(), name = 'index'),
  path('signup/', views.SignUp.as_view(), name = 'sign-up'),
  path('signin/', views.SignIn.as_view(), name = 'sign-in'),
  path('signout/', views.SignOut.as_view(), name = 'sign-out'),
  path('home/', views.Home.as_view(), name = 'home'),
  path('myrepo/', views.myRepo, name = 'my-repo'),
  path('users/', views.UserList.as_view(), name = 'user-list'),
  path('user/<str:id>/', views.UserDetail.as_view(), name = 'user-detail'),
]