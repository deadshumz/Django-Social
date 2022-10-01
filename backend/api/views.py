from rest_framework.response import Response
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from . import serializers
from .permissions import IsOwner


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

    def retrieve(self, request, *args, **kwargs):
        if kwargs.get('pk') == 'self' and request.user.is_authenticated:
            return Response(self.serializer_class(request.user).data)
        return super().retrieve(request, *args, **kwargs)

    def create(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)