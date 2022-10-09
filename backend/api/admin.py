from django.contrib import admin
from .models import CustomUser, Post


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    filter_horizontal = ('likes',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified',)
