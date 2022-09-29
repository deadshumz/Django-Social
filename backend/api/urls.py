from django.urls import path
from . import views

urlpatterns = [
    path("user", views.create_user),
    path("users", views.get_users),
]
