from django.shortcuts import render

# Create your views here.
from Facturacion.models import Empresa, DatosFacturacion
from OrdenesTrabajo.models import Orden


def ordenes_trabajo(request):
    mensaje=""
    empresa=Empresa.objects.get(usuario=request.user)
    datos = DatosFacturacion.objects.get(empresa=empresa)
    ordenes = Orden.objects.filter(empresa=empresa).count() + datos.secual_orden_trabajo + 1
    print(ordenes)
    if request.POST:
        print(request.POST)
        orden=None
        try:
            orden=Orden.objects.get(id=request.POST.get('idReg'))
            mensaje="El registro se ha actualizado exitosamente..!"
        except:
            orden=Orden()
            mensaje = "La Nueva orden de trabajo se registró..!"
        print(request.POST)
        orden.empresa=empresa
        orden.secuencial=request.POST.get('secuencial')
        orden.cliente_id=request.POST.get('id')
        orden.dispositivo_recibido = request.POST.get('dispositivo_recibido')
        orden.marca_modelo=request.POST.get('marca_modelo')
        orden.password=request.POST.get('password')
        orden.numero_serie=request.POST.get('numero_serie')
        orden.cables_accesorios=request.POST.get('cables_accesorios')
        orden.problema_reportado=request.POST.get('problema_reportado')
        orden.tareas_a_realizar=request.POST.get('solucion')
        orden.observaciones=request.POST.get('observaciones')
        orden.total=request.POST.get('total') or 0
        orden.abono=request.POST.get('abono') or 0
        orden.total_cobrar=request.POST.get('total_cobrar') or 0
        print(float(request.POST.get('total'))==float(request.POST.get('total')))
        if float(request.POST.get('total_cobrar'))==0.00:
            orden.estado="PAGADO"
        else:
            orden.estado=request.POST.get('estado') or "POR COBRAR"
        orden.save()
        print(orden)

    contexto={
        'empresa':empresa,
        'ordenes':Orden.objects.filter(empresa=empresa),
        'secuencial':str.zfill(str(ordenes), 9),
        'mensaje':mensaje,
    }
    return render(request,'ordenes_trabajo.html',contexto)