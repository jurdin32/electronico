from django.shortcuts import render

# Create your views here.
from Facturacion.models import Empresa
from OrdenesTrabajo.models import Orden


def ordenes_trabajo(request):
    empresa=Empresa.objects.get(usuario=request.user)
    contexto={
        'empresa':empresa,
        'ordenes':Orden.objects.filter(empresa=empresa)
    }
    return render(request,'ordenes_trabajo.html',contexto)