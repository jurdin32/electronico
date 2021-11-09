from django.core.mail import message
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from Facturacion.models import Empresa, PorcentajesImpuestos
from Productos.models import Producto


def registro_productos(request):
    empresa=Empresa.objects.get(usuario=request.user)
    mensaje=""
    if request.POST:
        print(request.POST)
        if request.POST.get('id'):
            impuesto=PorcentajesImpuestos.objects.get(id=request.POST.get('impuesto'))
            producto=Producto.objects.get(id=request.POST.get('id'))
            producto.descripcion=request.POST.get('descripcion')
            producto.impuesto=impuesto
            producto.precioUnitario=request.POST.get('precioUnitario').replace(",",".")
            if request.POST.get("activo"):
                producto.estado=True
            else:
                producto.estado=False
            producto.save()
            mensaje="El registro ha sido actualizado..!"
        else:
            impuesto = PorcentajesImpuestos.objects.get(id=request.POST.get('impuesto'))
            producto=Producto.objects.create(
                empresa=empresa,
                tipo = request.POST.get('tipo'),
                descripcion = request.POST.get('descripcion'),
                precioUnitario = request.POST.get('precioUnitario').replace(",","."),
                impuesto = impuesto,
                estado = True,
            )
            producto.save()
            mensaje = "Nuevo producto registrado..!"

    contexto={
        'empresa':empresa,
        'productos':Producto.objects.filter(empresa=empresa),
        'impuestos':PorcentajesImpuestos.objects.all(),
        'mensaje':mensaje
    }
    return render(request,'productos.html',contexto)
