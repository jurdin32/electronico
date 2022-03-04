from django.contrib.auth.models import User
from rest_framework import viewsets

from Personas.models import Clientes
from api.Personas.serializers import ClienteSerializers, UserSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClienteSerializers

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer