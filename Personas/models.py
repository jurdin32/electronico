from django.db import models

# Create your models here.
from Facturacion.models import Empresa
from electronico.configuracion import tipo_de_identificacion


class Clientes(models.Model):
    empresa=models.ForeignKey(Empresa,on_delete=models.CASCADE,null=True,blank=True)
    tipo_documento=models.CharField(max_length=2, choices=tipo_de_identificacion)
    nombres_apellidos=models.CharField(max_length=300)
    identificacion=models.CharField(max_length=13)
    direccion=models.CharField(max_length=300)
    telefono=models.CharField(max_length=13)
    correo_electronico=models.EmailField(max_length=300)
    estado=models.BooleanField(default=True)

    def __str__(self):
        return self.identificacion+" | "+self.nombres_apellidos
