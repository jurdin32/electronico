from io import BytesIO

from barcode.writer import ImageWriter
from django.core.files import File
from django.db import models
import barcode
# Create your models here.
from Facturacion.models import Empresa, PorcentajesImpuestos
from Personas.models import Clientes
from Productos.models import Producto

class Factura(models.Model):
    empresa=models.ForeignKey(Empresa,on_delete=models.CASCADE,null=True,blank=True)
    clave_acceso=models.CharField(max_length=49, default='0')
    secuencial=models.CharField(max_length=9,default="000000000",unique=True)
    cliente=models.ForeignKey(Clientes,on_delete=models.CASCADE)
    fecha=models.DateField(auto_now_add=True)
    totalSinImpuestos=models.DecimalField(max_digits=9, decimal_places=2,default=0)
    subtotal0=models.DecimalField(max_digits=9, decimal_places=2,default=0)
    subtotalimpuesto=models.DecimalField(max_digits=9, decimal_places=2,default=0)
    totalDescuento=models.DecimalField(max_digits=9, decimal_places=2,default=0)
    propina=models.DecimalField(max_digits=9, decimal_places=2,default=0)
    iva = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    importeTotal=models.DecimalField(max_digits=9, decimal_places=2,default=0)
    estado=models.CharField(max_length=100,default="",null=True,blank=True)
    documento=models.TextField(null=True,blank=True)
    mensajes=models.TextField(null=True,blank=True)


    firmado=models.BooleanField(default=False)
    enviado=models.BooleanField(default=False)

    def __str__(self):
        return self.empresa.razon_social_nombres_apellidos

class DetallesFactura(models.Model):
    factura=models.ForeignKey(Factura,on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad=models.DecimalField(default=0, decimal_places=2, max_digits=9)
    precioUnitario=models.DecimalField(max_digits=9, decimal_places=2,default=0)
    subtotal=models.DecimalField(max_digits=9, decimal_places=2,default=0)
    iva=models.DecimalField(max_digits=9, decimal_places=2,default=0)
    total=models.DecimalField(max_digits=9, decimal_places=2,default=0)

    def __str__(self):
        return self.producto.descripcion

class ImpuestosFactura(models.Model):
    factura=models.ForeignKey(Factura,on_delete=models.CASCADE)
    impuesto=models.ForeignKey(PorcentajesImpuestos,on_delete=models.CASCADE)
    subtotal=models.DecimalField(max_digits=9, decimal_places=2, default=0)
    total=models.DecimalField(max_digits=9, decimal_places=2, default=0)
