from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'users', views.CustomUserViewSet, basename="user")

urlpatterns = router.urls
