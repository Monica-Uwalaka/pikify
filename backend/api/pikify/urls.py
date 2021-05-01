"""
urls.py defines all the endpoints of our API service, as defined in the project requirements spec.
It also contains some extra endpoints for our own front-end client to use.
"""
from django.urls import path, include
from rest_framework import routers
from . import views

# Debug site/endpoints that DRF helps us implement.
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'', views.PikifyUserViewSet)

# Endpoint: /{dispaly_name}/
# GET: retrieve their profile
# POST: update profile
pikify_user = views.PikifyUserViewSet.as_view({
    'get': 'retrieve',
    'post': 'partial_update',
})

urlpatterns = [
  #path('', views.index, name='index'),
  path('', include(router.urls)),

  # Paths API endpoints
  path('<str:id>/', pikify_user, name='pikify_user'),

]