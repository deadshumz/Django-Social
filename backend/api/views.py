from rest_framework.response import Response
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

    def create(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)