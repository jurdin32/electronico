import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from DocumentosElectronicos.models import Factura

meses=[
    'Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'
]

def LoginView(request):
    if request.POST:
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'),is_active=True)
        if user:
            login(request,user)
            return HttpResponseRedirect("/")
    else:
        return render(request, 'login.html')

@login_required(login_url='/login')
def LogoutView(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='login')
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
