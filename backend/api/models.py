from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars", blank=True)
    bio = models.TextField(max_length=256, blank=True, default="default bio")

    def save(self, *args, **kwargs):
        # Checking if bio empty then setting it to default value
        if not self.bio:
            default_bio = self._meta.get_field("bio").default
            self.bio = default_bio
            self.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username
