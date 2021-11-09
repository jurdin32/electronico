from django.contrib import admin

# Register your models here.
from Personas.models import Clientes
from electronico.snniper import Attr

@admin.register(Clientes)
class modelo(admin.ModelAdmin):
    list_display = Attr(Clientes)
    list_display_links = Attr(Clientes)