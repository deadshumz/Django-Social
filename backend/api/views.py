from asgiref.sync import sync_to_async
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import ( UserSerializer )

# Create your views here.
@sync_to_async
@api_view(['GET'])
def get_users(request):
    queryset = User.objects.all()
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)