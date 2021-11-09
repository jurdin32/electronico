import datetime

from django.db.models import Count, Sum
from django.shortcuts import render

# Create your views here.
from DocumentosElectronicos.models import Factura

meses=[
    'Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'
]

def index(request):
    fecha_actual=datetime.datetime.now()
    facturas=Factura.objects.filter(empresa__usuario=request.user, fecha__month=fecha_actual.month)
    print(facturas.filter(fecha=fecha_actual.date()).values('fecha').annotate(Sum('importeTotal')))
    contexto={
        'facturas':facturas.values('fecha').annotate(Sum('importeTotal')),
        'deldia':facturas.filter(fecha=fecha_actual.date()).values('fecha').annotate(Sum('importeTotal')),
        'mes':meses[fecha_actual.month-1],
        'año':fecha_actual.year

    }

    return render(request,'index.html',contexto)
