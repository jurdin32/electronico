from django.contrib import admin

# Register your models here.
from OrdenesTrabajo.models import Orden
from electronico.snniper import Attr

@admin.register(Orden)
class modelo(admin.ModelAdmin):
    list_display = Attr(Orden)
    list_display_links = Attr(Orden)