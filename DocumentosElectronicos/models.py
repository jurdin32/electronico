from django.db import models
from Facturacion.models import Empresa, PorcentajesImpuestos, FormasPagos
from Personas.models import Clientes
from Productos.models import Producto

class Factura(models.Model):
    tipo=models.CharField(max_length=20, default="FACTURA")
    formaPago=models.ForeignKey(FormasPagos,on_delete=models.CASCADE, default=1)
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
        return self.cliente.nombres_apellidos

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

class CuentaCobrar(models.Model):
    fecha=models.DateField(auto_now_add=True)
    documento=models.ForeignKey(Factura,on_delete=models.CASCADE)
    detalle=models.TextField(null=True,blank=True)
    estado=models.CharField(max_length=20, default="DEBE")

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.detalle="Cuenta por cobrar según %s No. %s"%(self.documento.tipo, self.documento.secuencial)
        super(CuentaCobrar, self).save()

class DetalleCuentasCobrar(models.Model):
    fecha=models.DateField(auto_now_add=True)
    cuenta=models.ForeignKey(CuentaCobrar, on_delete=models.CASCADE)
    no_abono=models.CharField(max_length=20,null=True,blank=True)
    saldo_anterior=models.DecimalField(max_digits=9, decimal_places=2, default=0)
    abono=models.DecimalField(max_digits=9, decimal_places=2, default=0)
    por_pagar=models.DecimalField(max_digits=9, decimal_places=2, default=0)
    pago_no=models.IntegerField(default=0)
    tipo=models.CharField(max_length=120, null= True, blank=True)
    detalle=models.CharField(max_length=500, null= True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.por_pagar==0:
            self.cuenta.estado="PAGADO"
            self.cuenta.save()
        else:
            self.cuenta.estado = "DEBE"
            self.cuenta.save()
        super(DetalleCuentasCobrar, self).save()



