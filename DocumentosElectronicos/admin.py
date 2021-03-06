from django.contrib import admin

# Register your models here.
from DocumentosElectronicos.models import Factura, DetallesFactura, CuentaCobrar, DetalleCuentasCobrar
from electronico.snniper import Attr

class DetallesInline(admin.StackedInline):
    model = DetallesFactura
    extra = 0

@admin.register(Factura)
class modelo(admin.ModelAdmin):
    list_display_links = Attr(Factura)
    list_display = Attr(Factura)
    inlines = [DetallesInline]


@admin.register(DetallesFactura)
class modelo(admin.ModelAdmin):
    list_display_links = Attr(DetallesFactura)
    list_display = Attr(DetallesFactura)


class DetallesCuentasInline(admin.StackedInline):
    model = DetalleCuentasCobrar
    extra = 0


@admin.register(CuentaCobrar)
class modelo(admin.ModelAdmin):
    list_display_links = Attr(CuentaCobrar)
    list_display = Attr(CuentaCobrar)
    inlines = [DetallesCuentasInline]