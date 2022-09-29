from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from . import serializers


@api_view(["GET"])
def get_users(request):
    queryset = User.objects.all()
    serializer = serializers.UserSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_user(request, fromat='json'):
    serializer = serializers.CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        if user:
            return Response(serializer.data)
    else:
        return Response('Username is already taken')