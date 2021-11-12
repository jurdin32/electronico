from django.db import models

# Create your models here.
from Personas.models import Clientes


class Orden(models.Model):
    fecha=models.DateTimeField(auto_now_add=True)
    secuencial=models.CharField(max_length=9, default='000000000')
    cliente=models.ForeignKey(Clientes,on_delete=models.CASCADE)
    dispositivo_recibido=models.TextField()
    marca_modelo=models.TextField(null=True,blank=True)
    password=models.CharField(max_length=50,null=True,blank=True)
    numero_serie=models.CharField(max_length=50,null=True,blank=True)
    cables_accesorios=models.TextField(null=True,blank=True)
    problema_reportado=models.TextField(null=True,blank=True)
    tareas_a_realizar=models.TextField(null=True,blank=True)
    observaciones=models.TextField(null=True,blank=True)
    hora_fecha_salida=models.DateTimeField(null=True,blank=True)
    estado=models.CharField(max_length=60,default="EN REVISIÓN")
