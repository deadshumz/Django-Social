from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to="avatars", blank=True)
    bio = models.TextField(max_length=256, blank=True, default="default bio")
    likes = models.ManyToManyField('Post', blank=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    image = models.ImageField(upload_to="posts", blank=False)
    description = models.TextField(max_length=256, blank=True)