from django.contrib import admin

# Register your models here.
from Facturacion.models import Empresa, Impuestos, PorcentajesImpuestos, DatosFacturacion, Webservices, FormasPagos
from electronico.snniper import Attr


@admin.register(Empresa)
class modelo(admin.ModelAdmin):
    list_display = Attr(Empresa)
    list_display_links = Attr(Empresa)

@admin.register(Impuestos)
class modelo(admin.ModelAdmin):
    list_display = Attr(Impuestos)
    list_display_links = Attr(Impuestos)

@admin.register(PorcentajesImpuestos)
class modelo(admin.ModelAdmin):
    list_display = Attr(PorcentajesImpuestos)
    list_display_links = Attr(PorcentajesImpuestos)

@admin.register(DatosFacturacion)
class modelo(admin.ModelAdmin):
    list_display = Attr(DatosFacturacion)
    list_display_links = Attr(DatosFacturacion)

@admin.register(Webservices)
class modelo(admin.ModelAdmin):
    list_display = Attr(Webservices)
    list_display_links = Attr(Webservices)

@admin.register(FormasPagos)
class modelo(admin.ModelAdmin):
    list_display = Attr(FormasPagos)
    list_display_links = Attr(FormasPagos)
