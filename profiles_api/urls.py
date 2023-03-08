from django.urls import path, include
from rest_framework import routers
# from rest_framework import DefaultRouter
from profiles_api import views


router = routers.DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))

]