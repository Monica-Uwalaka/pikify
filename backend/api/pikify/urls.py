"""
urls.py defines all the endpoints of our API service, as defined in the project requirements spec.
It also contains some extra endpoints for our own front-end client to use.
"""
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static


# Debug site/endpoints that DRF helps us implement.
# Routers provide an easy way of automatically determining the URL conf.


urlpatterns = [
  # Paths API endpoints
  #pikify Home page
  path('', views.Index.as_view(), name = 'index'),
  path('signup/', views.SignUp.as_view(), name = 'sign-up'),
  path('signin/', auth_views.LoginView.as_view(template_name = 'pikify/signin.html'), name = 'sign-in'),
  path('signout/', auth_views.LogoutView.as_view(template_name = 'pikify/signout.html'), name = 'sign-out'),
  path('home/', views.Home.as_view(), name = 'home'),
  path('search/', views.Search.as_view(), name = 'search'),
  path('profile/', views.Profile.as_view(), name = 'profile'),
  path('myrepo/', views.MyRepo.as_view(), name = 'my-repo'),
  path('users/', views.UserList.as_view(), name = 'user-list'),
  path('user/<str:id>/', views.UserDetail.as_view(), name = 'user-detail'),
]


if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
