from django.contrib import admin

# Register your models here.
from Productos.models import Producto, Kardex
from electronico.snniper import Attr


@admin.register(Producto)
class modelo(admin.ModelAdmin):
    list_display_links = Attr(Producto)
    list_display = Attr(Producto)

@admin.register(Kardex)
class modelo(admin.ModelAdmin):
    list_display_links = Attr(Kardex)
    list_display = Attr(Kardex)