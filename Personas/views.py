from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from simple_search import search_filter
from django.core import serializers
# Create your views here.
from Facturacion.models import Empresa
from Personas.models import Clientes

def buscar_cliente(request):
    clientes=Clientes.objects.filter(empresa__usuario=request.user, estado=True)
    if request.GET.get('q'):
        fields=['identificacion','nombres_apellidos']
        clientes=serializers.serialize('json',clientes.filter(search_filter(fields, str.upper(request.GET.get('q')))))
    else:
        clientes = serializers.serialize('json',clientes)
    return JsonResponse(clientes,safe=False)

def clientes(request):
    mensaje=""
    empresa=Empresa.objects.get(usuario=request.user)
    if request.POST:
        cliente=Clientes()
        if request.POST.get('id'):
            cliente=Clientes.objects.get(id=request.POST.get('id'))
            mensaje="El registro se ha actualizado correctamente..!"
        else:
            mensaje="Un cliente se ha registrado en la base de datos..!"
        cliente.empresa_id=empresa.id
        cliente.tipo_documento = request.POST.get('tipo')
        cliente.identificacion = request.POST.get('identificacion')
        cliente.nombres_apellidos = request.POST.get('nombres')
        cliente.direccion = request.POST.get('direccion')
        cliente.telefono = request.POST.get('telefono')
        cliente.correo_electronico = request.POST.get('correo')
        if request.POST.get("activo"):
            cliente.estado = True
        else:
            cliente.estado = False
        cliente.save()
    contexto={
        'clientes':Clientes.objects.filter(empresa__usuario=request.user),
        'mensaje':mensaje
    }
    return render(request,'clientes.html',contexto)