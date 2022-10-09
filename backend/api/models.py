from django.db import models
from django.contrib.auth.models import AbstractUser


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to="avatars", blank=True)
    bio = models.TextField(max_length=256, blank=True, default="default bio")
    likes = models.ManyToManyField('Post', blank=True)

    def __str__(self):
        return self.username


class Post(TimeStampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="posts", blank=False)
    description = models.TextField(max_length=256, blank=True)

    def __str__(self):
        return f"{str(self.user).capitalize()}'s post №{self.pk}"