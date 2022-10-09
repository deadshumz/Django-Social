from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import CustomUser, Post
from . import serializers


class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CustomUserSerializer
    queryset = CustomUser.objects.all()

    def retrieve(self, request, *args, **kwargs):
        if kwargs.get('pk') == 'self' and request.user.is_authenticated:
            return Response(self.serializer_class(request.user).data)
        return super().retrieve(request, *args, **kwargs)

    def create(self, request):
        serializer = serializers.CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PostSerializer
    queryset = Post.objects.all()
