from django import template
from django.db.models import Sum

from Productos.models import Kardex

register = template.Library()

@register.simple_tag
def CalcularStock(id_producto):
    todo=Kardex.objects.filter(producto_id=id_producto)
    ingreso=todo.filter(tipo="I").aggregate(Sum('cantidad'))
    egreso=todo.filter(tipo="S").aggregate(Sum('cantidad'))
    if ingreso['cantidad__sum']:
        ingreso=ingreso['cantidad__sum']
    else:
        ingreso=0
    if egreso['cantidad__sum']:
        egreso = egreso['cantidad__sum']
    else:
        egreso = 0
    return ingreso-egreso
