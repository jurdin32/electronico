from rest_framework import viewsets

from Facturacion.models import Empresa
from api.Empresa.serializers import EmpresaSerializers



class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class =EmpresaSerializers