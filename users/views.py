from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UsersViewSet(viewsets.ModelViewSet):
    # Minimamente hay que pasar queryset y serializer_class
    queryset = User.objects.all()
    serializer_class = UserSerializer