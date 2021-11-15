from django.db import models

# Create your models here.
from Facturacion.models import DatosFacturacion, Empresa
from Personas.models import Clientes


class Orden(models.Model):
    empresa=models.ForeignKey(Empresa,on_delete=models.CASCADE,null=True,blank=True)
    fecha=models.DateTimeField(auto_now_add=True)
    secuencial=models.CharField(max_length=9,null=True,blank=True)
    cliente=models.ForeignKey(Clientes,on_delete=models.CASCADE)
    dispositivo_recibido=models.TextField()
    marca_modelo=models.TextField(null=True,blank=True)
    password=models.CharField(max_length=50,null=True,blank=True)
    numero_serie=models.CharField(max_length=50,null=True,blank=True)
    cables_accesorios=models.TextField(null=True,blank=True)
    problema_reportado=models.TextField(null=True,blank=True)
    tareas_a_realizar=models.TextField(null=True,blank=True)
    observaciones=models.TextField(null=True,blank=True)
    hora_fecha_salida=models.DateTimeField(auto_now=True)
    total=models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    abono=models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    total_cobrar=models.DecimalField(max_digits=9,decimal_places=2, default=0.00)
    estado=models.CharField(max_length=60,default="EN REVISIÓN")

    def __str__(self):
        return self.secuencial

