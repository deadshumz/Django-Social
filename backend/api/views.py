from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import UserSerializer


@api_view(["GET"])
def get_users(request):
    queryset = User.objects.all()
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)


# @api_view(['POST'])
# def create_user(request):
