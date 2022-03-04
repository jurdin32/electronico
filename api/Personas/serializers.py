from django.contrib.auth.models import User
from rest_framework import serializers
from Personas.models import Clientes

class ClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['id','username','first_name','last_name','is_staff','is_active']
