from django.db import models

# Create your models here.
from Facturacion.models import *

class Producto(models.Model):
    empresa=models.ForeignKey(Empresa,on_delete=models.CASCADE,null=True,blank=True)
    tipo=models.CharField(max_length=12, choices=(("S","Servicios"),("P","Productos")))
    codigoAuxiliar=models.CharField(max_length=25,null=True,blank=True)
    descripcion=models.CharField(max_length=300)
    cantidad=models.IntegerField(default=1)
    precioUnitario=models.DecimalField(default=0.00,decimal_places=2,max_digits=9)
    descuento = models.DecimalField(default=0.00, decimal_places=2, max_digits=9)
    impuesto=models.ForeignKey(PorcentajesImpuestos,on_delete=models.CASCADE,null=True,blank=True)
    valor_impuesto=models.DecimalField(default=0.00, decimal_places=2, max_digits=9)
    total=models.DecimalField(default=0.00, decimal_places=2, max_digits=9)
    estado=models.BooleanField(default=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.descripcion=str.upper(self.descripcion).encode('utf-8')
        if not self.codigoAuxiliar:
            contador=Producto.objects.filter(tipo=self.tipo).count()+1
            self.codigoAuxiliar=self.tipo+str.zfill(str(contador),6)
        precio=float(self.precioUnitario)
        iva=precio*float(self.impuesto.porcentaje)
        total=precio+iva
        self.valor_impuesto=iva
        self.total=total
        
        super(Producto, self).save()

    def __str__(self):
        return "%s, %s"%(self.descripcion,self.total)

    class Meta:
        verbose_name_plural="1. Productos"

class Kardex(models.Model):
    tipo=models.CharField(max_length=1, choices=(("I","Ingreso"),("S","Salida")))
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    detalle=models.TextField()

    class Meta:
        verbose_name_plural="1.1 Kardex"

