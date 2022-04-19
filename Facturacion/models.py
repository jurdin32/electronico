from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class FormasPagos(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(default=0, max_length=2)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "1. Formas de Pago"

    def __str__(self):
        return self.nombre


class Impuestos(models.Model):
    nombre=models.CharField(max_length=10)
    codigo=models.IntegerField(default=0)

    class Meta:
        verbose_name_plural="2. Codigos de Impuestos"

    def __str__(self):
        return self.nombre

class PorcentajesImpuestos(models.Model):
    impuesto=models.ForeignKey(Impuestos,on_delete=models.CASCADE,null=True,blank=True)
    porcentaje=models.DecimalField(max_digits=9, decimal_places=2,default=0)
    nombre=models.CharField(max_length=100)
    codigo=models.IntegerField(default=0)
    default=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural="2.1 Porcentajes de Impuestos"

    def __str__(self):
        return self.impuesto.nombre+" | "+self.nombre


class Empresa(models.Model):
    usuario=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    ruc=models.CharField(max_length=13)
    razon_social_nombres_apellidos=models.CharField(max_length=300)
    nombre_comercial=models.CharField(max_length=300,null=True,blank=True)
    direccion_establecimiento_matriz=models.CharField(max_length=300)
    direccion_establecimiento_emisor=models.CharField(max_length=300,null=True,blank=True)
    codigo_establecimiento_emisior=models.CharField(max_length=3)
    punto_emision_establecimiento=models.CharField(max_length=3)
    contribuyente_especial=models.CharField(max_length=5,null=True,blank=True, help_text='minimo 3, maximo 5')
    obligado_llevar_contabilidad=models.CharField(max_length=2, choices=(("SI","SI"),("NO","NO")))
    logotipo=models.ImageField(upload_to='logotipo',null=True,blank=True)
    encabezado=models.ImageField(upload_to='encabezado',null=True,blank=True)
    tipo_emision=models.CharField(max_length=1,default=1)
    estado=models.BooleanField(default=True)

    def __str__(self):
        return "%s"%(self.razon_social_nombres_apellidos)

    class Meta:
        verbose_name_plural="4. Empresa"


class Webservices(models.Model):
    empresa=models.ForeignKey(Empresa,on_delete=models.CASCADE,null=True,blank=True)
    tipo_ambiente=models.IntegerField(default=1, choices=((1,"PRUEBAS"),(2,"PRODUCCIÓN")))
    webservice=models.TextField()
    envio_consulta=models.IntegerField(default=1, help_text="1 para enviar al sri, 2 para consultar")#1 consulta 2 envio
    estado=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural="3. Webservices"

class DatosFacturacion(models.Model):
    empresa=models.ForeignKey(Empresa,on_delete=models.CASCADE,null=True,blank=True)
    secuencial=models.IntegerField(default=0)
    secuencial_proforma=models.IntegerField(default=0)
    secual_orden_trabajo=models.IntegerField(default=1)
    ambiente=models.IntegerField(choices=((1,"PRUEBAS"),(2,"PRODUCCIÓN")))
    certificado=models.FileField(upload_to='certificados',null=True,blank=True)
    clave=models.CharField(max_length=100, default="")
    ruta_home_media=models.CharField(max_length=1000,default='/home/johnny/media/')
    usa_facturacion_electronica=models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        webservices=Webservices.objects.all()
        for webservice in webservices.all():
            webservice.estado=False
            webservice.save()
        if self.ambiente==1:
            for web in webservices.filter(tipo_ambiente=1):
                web.estado=True
                web.save()
        if self.ambiente==2:
            for web in webservices.filter(tipo_ambiente=2):
                web.estado = True
                web.save()



        super(DatosFacturacion, self).save()

    class Meta:
        verbose_name_plural="5. Datos de la Facturación"
