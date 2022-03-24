#!/usr/bin/python
#-*- coding: utf-8 -*-

import os, sys
import datetime
import subprocess
from xml.dom.minidom import parseString

import qrcode
import zeep as zeep
from dicttoxml import dicttoxml
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.shortcuts import render

from DocumentosElectronicos.models import Factura, DetallesFactura, CuentaCobrar, DetalleCuentasCobrar
from Facturacion.models import DatosFacturacion, Webservices, Empresa, FormasPagos
from Facturacion.script import modulo_11
from Productos.models import Kardex, Producto
from electronico.snniper import render_to_pdf


def generarFactura(factura_id):
    factura = Factura.objects.get(id=factura_id)
    infoTributaria = {}
    infoFactura = {}
    datos = factura.empresa
    datos_factura = DatosFacturacion.objects.get(empresa=datos)
    cantidad = Factura.objects.count()
    secuencial = str.zfill(str(datos_factura.secuencial + cantidad), 9)
    ambiente = Webservices.objects.get(empresa=datos, estado=True, envio_consulta=1)
    print(secuencial)
    clave_acceso = modulo_11('01', factura.empresa.ruc, ambiente.tipo_ambiente, datos.codigo_establecimiento_emisior,
                             datos.punto_emision_establecimiento, secuencial, '00000000')
    now = datetime.datetime.now()
    fecha = now.strftime('%d/%m/%Y')
    # detalles:
    detalles = ""
    baseImponible = 0
    total_iva = 0
    total = 0
    detallesF=DetallesFactura.objects.filter(factura=factura)
    for detalle in detallesF:
        detalles += """<detalle>
                    <codigoPrincipal>%s</codigoPrincipal>
                    <codigoAuxiliar>%s</codigoAuxiliar>
                    <descripcion>%s</descripcion>
                    <cantidad>%s</cantidad>
                    <precioUnitario>%s</precioUnitario>
                    <descuento>0.00</descuento>
                    <precioTotalSinImpuesto>%s</precioTotalSinImpuesto>
                    <impuestos>
                        <impuesto>
                            <codigo>%s</codigo>
                            <codigoPorcentaje>%s</codigoPorcentaje>
                            <tarifa>%s</tarifa>
                            <baseImponible>%s</baseImponible>
                            <valor>%s</valor>
                        </impuesto>
                    </impuestos>
                </detalle>""" % (
        detalle.producto_id, detalle.producto.codigoAuxiliar, detalle.producto.descripcion, detalle.cantidad,
        round(detalle.precioUnitario,2), round(detalle.subtotal,2), detalle.producto.impuesto.impuesto.codigo,
        detalle.producto.impuesto.codigo, round(detalle.producto.impuesto.porcentaje * 100,2), round(detalle.subtotal,2),
        round(detalle.iva,2))
        baseImponible += float(detalle.subtotal)
        total_iva += float(detalle.iva)
        total += float(detalle.total)
    factura.clave_acceso = clave_acceso
    # factura.totalSinImpuestos = baseImponible
    # factura.iva = total_iva
    factura.importeTotal = total
    factura.save()
    # vendedor
    infoTributaria.setdefault('ambiente', ambiente.tipo_ambiente)
    infoTributaria.setdefault('tipoEmision', 1)
    infoTributaria.setdefault('razonSocial', datos.razon_social_nombres_apellidos)
    infoTributaria.setdefault('nombreComercial', datos.nombre_comercial)
    infoTributaria.setdefault('ruc', datos.ruc)
    infoTributaria.setdefault('claveAcceso', clave_acceso)
    infoTributaria.setdefault('codDoc', '01')  # factura
    infoTributaria.setdefault('estab', datos.codigo_establecimiento_emisior)
    infoTributaria.setdefault('ptoEmi', datos.punto_emision_establecimiento)
    infoTributaria.setdefault('secuencial', secuencial)
    infoTributaria.setdefault('dirMatriz', datos.direccion_establecimiento_matriz)
    infoFactura.setdefault('fechaEmision', fecha)
    infoFactura.setdefault('dirEstablecimiento', datos.direccion_establecimiento_emisor)
    infoFactura.setdefault('obligadoContabilidad', datos.obligado_llevar_contabilidad)
    # cliente
    infoFactura.setdefault('tipoIdentificacionComprador',
                           factura.cliente.tipo_documento)  # si es cedula ruc u otro esto es del cliente
    infoFactura.setdefault('razonSocialComprador', factura.cliente.nombres_apellidos)
    infoFactura.setdefault('identificacionComprador', factura.cliente.identificacion)
    infoFactura.setdefault('direccionComprador', factura.cliente.direccion)
    infoFactura.setdefault('totalSinImpuestos', baseImponible)
    infoFactura.setdefault('totalDescuento', '0.00')
    totalImpuesto=[]
    for fd in DetallesFactura.objects.filter(factura_id=factura_id).values('producto__impuesto__impuesto__codigo','producto__impuesto__codigo').annotate(Sum('subtotal')).annotate(Sum('iva')):
        totalImpuesto.append({
            'codigo':fd['producto__impuesto__impuesto__codigo'],
            'codigoPorcentaje':fd['producto__impuesto__codigo'],
            'baseImponible':fd['subtotal__sum'],
            'valor':round(fd['iva__sum'],2),
        })
    print(totalImpuesto)
    infoFactura.setdefault('totalConImpuestos', totalImpuesto)  # aqui van todos los impuestos
    infoFactura.setdefault('propina', '0.00')
    infoFactura.setdefault('importeTotal', round(total,2))  # suma total
    infoFactura.setdefault('moneda', 'DOLAR')
    infoFactura.setdefault('pagos', {'pago': {
        'formaPago': factura.formaPago.codigo,  # forma de pago segun la tabla 24
        'total': round(total,2),
        'plazo': 1,  # plazo en dias
        'unidadTiempo': 'dias'
    }})

    factura = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <factura id='comprobante' version='1.0.0'>
            <infoTributaria>
                val1
            </infoTributaria>
            <infoFactura>
                val2
            </infoFactura>
            <detalles>
                val3
            </detalles>
        </factura>""".replace('val1', str(dicttoxml(infoTributaria, attr_type=False, root=False))).replace('val2',
                                                                                                           str(dicttoxml(
                                                                                                               infoFactura,
                                                                                                               attr_type=False,
                                                                                                               root=False))).replace(
        "b'", "").replace(">'", ">").replace('val3', detalles).replace("<item>","<totalImpuesto>").replace("</item>","</totalImpuesto>")
    path = '%s/xml/%s.xml' % (datos_factura.ruta_home_media,clave_acceso)
    xml = open(path, 'w')
    factura = parseString(factura)
    xml.write(factura.toprettyxml())
    xml.close()


def firmar_documento(request):
    if request.GET.get('id'):
        factura = Factura.objects.get(id=request.GET.get('id'))
        datos = DatosFacturacion.objects.get(empresa=factura.empresa)
        try:
            javapath = '%s/Java/Linux/jdk1.7.0_80/bin/java'%datos.ruta_home_media
            java = '%s/Java/comprobantes.jar'%datos.ruta_home_media
            path = '%s/xml/%s.xml' % (datos.ruta_home_media,factura.clave_acceso)
            path_salida = '%s/firmado'%datos.ruta_home_media
            args = [java, path, datos.certificado.path, datos.clave, path_salida, factura.clave_acceso + ".xml"]
            subprocess.run([javapath, '-jar'] + args)
            factura.firmado = True
            factura.save()
            return HttpResponse('FIRMADO')
        except Exception as error:
            print(error)
            return HttpResponse(error)

def enviar_sri(request):
    webservice = Webservices.objects.get(empresa__usuario=request.user, estado=True, envio_consulta=1)

    if request.GET.get('fac'):
        factura=Factura.objects.get(clave_acceso=request.GET.get('fac'))
        datos = DatosFacturacion.objects.get(empresa=factura.empresa)
        try:
            print('Ambiente', webservice.webservice, webservice.tipo_ambiente)
            path = '%s/firmado/%s.xml' % (datos.ruta_home_media,request.GET.get('fac'))
            respuestas ='%s/firmado/%s.json' % (datos.ruta_home_media,request.GET.get('fac'))
            print(path)
            comprobante = open(path, "rb")  # apertura del archivo xml
            xmlBytes = comprobante.read()  # creando mapa de bits del comprobante
            client = zeep.Client(wsdl=webservice.webservice)  # creando una instancia de zeep cliente
            print("Inicia el proceso de envio..!!")
            result = client.service.validarComprobante(xmlBytes)
            jsonarchivo = open(respuestas, "w")
            jsonarchivo.write(str(result))
            jsonarchivo.close()
            factura.enviado = True
            factura.save()
            print("Respuesta: ", result)  # respuesta del servidor
            consulta_comprobantes(request)
        except Exception as error:
            print(error)
    return HttpResponse(webservice.tipo_ambiente)

def crear_archivos(path,json,formato):
    archivo = open(path+'.'+formato, 'w')
    archivo.write(str(json))
    archivo.close()

def consulta_comprobantes(request):
    webservice = Webservices.objects.get(empresa__usuario=request.user, estado=True, envio_consulta=2)
    client = zeep.Client(wsdl=webservice.webservice)
    json = client.service.autorizacionComprobante(request.GET.get('fac'))
    if request.GET.get('fac'):
        factura=Factura.objects.get(clave_acceso=request.GET.get('fac'))
        datos = DatosFacturacion.objects.get(empresa=factura.empresa)
        path = '%s/autorizados/%s' % (datos.ruta_home_media,request.GET.get('fac'))
        crear_archivos(path,json['autorizaciones']['autorizacion'][0]['comprobante'],'xml')
        crear_archivos(path,u''.join(json).encode('utf-8').strip(),'json')
        try:
            factura = Factura.objects.get(clave_acceso=request.GET.get('fac'))
            factura.documento = json
            factura.estado = json['autorizaciones']['autorizacion'][0]['estado']
            factura.mensajes = json['autorizaciones']['autorizacion'][0]['mensajes']
            factura.save()
        except:
            print(json)
        print(json)
    return HttpResponseRedirect('/fac/list/')

@login_required(login_url='login')
def facturacion(request):
    cantidad=0
    secuencial=""
    datos_factura = DatosFacturacion.objects.get(empresa__usuario=request.user)
    if request.GET.get('type')=='factura':
        cantidad = Factura.objects.filter(tipo="FACTURA").count()
        secuencial = str.zfill(str(datos_factura.secuencial + cantidad + 1), 9)
    else:
        cantidad = Factura.objects.filter(tipo="PROFORMA").count()
        secuencial = str.zfill(str(datos_factura.secuencial_proforma + cantidad + 1), 9)

    contexto = {
        'datos':datos_factura.usa_facturacion_electronica,
        'secuencial': secuencial,
        'establecimiento': datos_factura.empresa.codigo_establecimiento_emisior,
        'puntoEmision': datos_factura.empresa.punto_emision_establecimiento,
        'ambiente': datos_factura.ambiente,
        'productos':Producto.objects.filter(empresa__usuario=request.user, estado=True),
        'tipo':request.GET.get('type'),
        'empresa': Empresa.objects.get(usuario=request.user),
        'formasPago':FormasPagos.objects.filter(estado=True),
    }
    return render(request, 'facturacion.html', contexto)


def registroFactura(request):
    datos = DatosFacturacion.objects.get(empresa__usuario=request.user)
    fac = Factura.objects.create(
        tipo=request.GET.get('tipo'),
        formaPago_id=request.GET.get('fpago'),
        secuencial=request.GET.get('secuencial'),
        cliente_id=request.GET.get('id_cliente'),
        empresa_id=datos.empresa_id,
        totalSinImpuestos=request.GET.get('totalSinImpuestos'),
        iva=request.GET.get('iva'),
        importeTotal=request.GET.get('importeTotal'),
    )
    fac.save()
    return HttpResponse(fac.id)


def registroDetalles(request):
    det = DetallesFactura.objects.create(
        factura_id=request.GET.get('factura_id'),
        producto_id=request.GET.get('producto_id'),
        cantidad=request.GET.get('cantidad'),
        precioUnitario=request.GET.get('precioUnitario'),
        subtotal=request.GET.get('subtotal'),
        iva=request.GET.get('iva'),
        total=request.GET.get('total')
    )
    det.save()
    fac=Factura.objects.get(id=request.GET.get('factura_id'))
    if float(det.producto.impuesto.porcentaje)==0.00:
        fac.subtotal0=float(fac.subtotal0)+float(det.subtotal)
        fac.save()
    else:
        fac.subtotalimpuesto=float(fac.subtotalimpuesto)+float(det.subtotal)
        fac.save()
    kardex = Kardex.objects.create(
        tipo="S",
        producto_id=request.GET.get('producto_id'),
        cantidad=request.GET.get('cantidad'),
        detalle="Para registrar venta segun factura no. %s por un valor de %s, con fecha %s al cliente %s" % (
        det.factura.secuencial, det.factura.importeTotal, det.factura.fecha, det.factura.cliente.nombres_apellidos)
    )
    kardex.save()
    generarFactura(det.factura_id)
    return HttpResponse('ok')

def facturas(request):
    contexto = {
        'facturas': Factura.objects.filter(empresa__usuario=request.user).order_by('-fecha'),
        'datos':DatosFacturacion.objects.get(empresa__usuario=request.user),
        'empresa': Empresa.objects.get(usuario=request.user),
    }
    return render(request, 'facturas.html', contexto)

def ride(request):
    factura=None
    fecha=""
    ambiente=""
    detalles=None
    try:
        factura=Factura.objects.get(clave_acceso=request.GET.get('clave'))
        detalles=DetallesFactura.objects.filter(factura=factura)
        webservice = Webservices.objects.get(empresa__usuario=request.user, estado=True, envio_consulta=2)
        client = zeep.Client(wsdl=webservice.webservice)
        json = client.service.autorizacionComprobante(request.GET.get('clave'))
        fecha=json['autorizaciones']['autorizacion'][0]['fechaAutorizacion']
        ambiente=json['autorizaciones']['autorizacion'][0]['ambiente']
        factura.ambiente=json['autorizaciones']['autorizacion'][0]['ambiente']
        factura.save()
        #print(json)

    except:
        pass
    contexto={
        'factura':factura,
        'fecha':fecha,
        'ambiente':ambiente,
        'detalles':detalles,
    }
    #return render(request,'ride.html',contexto)
    return render_to_pdf('ride.html',contexto)

def cuentasCobrar(request):
    cuentas=CuentaCobrar.objects.filter(documento__empresa__usuario=request.user)
    cuenta=None
    if request.GET.get('id'):
        cuenta=cuentas.get(id=request.GET.get('id'))

    contexto={
        'cuentas':cuentas,
        'detalles':DetalleCuentasCobrar.objects.filter(cuenta_id=request.GET.get('id')),
        'cuenta':cuenta,
        'documentos':Factura.objects.filter(empresa__usuario=request.user),
        'empresa': Empresa.objects.get(usuario=request.user),
    }
    return render(request, 'ctasCobrar.html',contexto)

def registar_cuenta(request,id):
    cuenta=CuentaCobrar.objects.create(documento_id=id)
    cuenta.save()
    messages.add_message(request, messages.SUCCESS, 'La Cuenta se registro Correctamente..!')
    return HttpResponseRedirect("/counts/?id=%s"%cuenta.id)

def crearQr(documento,anterior,abono,saldo,cliente):
    img = qrcode.make("DOCUMENTO FIRMADO ELECTRONICAMENTE\nJOHNNY EDGAR URDIN GONZALEZ\nRUC: 0703886697\nREGISTRO DEL CREDITO PARA EL CLIENTE: %s\nFECHA: %s\nSALDO ANTERIOR %s\nABONO: %s\nPOR PAGAR: %s\nESTADO DEL DOCUMENTO: PAGADO"%(cliente,datetime.datetime.now(),anterior,abono,saldo))
    f = open("/mnt/07EBF45679F193CD/var/www/electronico/media/codigoQR/%s.png"%documento, "wb")
    img.save(f)
    f.close()

def registarAbono(request):
    if request.POST:
        print(request.POST)
        cuenta=CuentaCobrar.objects.get(id=request.POST.get('cuenta'))
        detalles= DetalleCuentasCobrar.objects.filter(cuenta=cuenta)
        cant=detalles.count()+1
        por_pagar=0
        anterior=0
        if cant==1:
            anterior=float(cuenta.documento.importeTotal)
            por_pagar = float(cuenta.documento.importeTotal) - float(request.POST.get('abono'))
        else:
            anterior=detalles.last().por_pagar
            por_pagar = float(anterior) - float(request.POST.get('abono'))

        abono=DetalleCuentasCobrar.objects.create(
            cuenta=cuenta,
            abono=request.POST.get('abono'),
            no_abono = "%s-%s" % (cuenta.documento.secuencial, cant),
            por_pagar=por_pagar,
            pago_no=cant,
            saldo_anterior=anterior,
            tipo=request.POST.get('tipo'),
            detalle=request.POST.get('detalle'),
        )
        abono.save()
        crearQr(abono.no_abono,abono.saldo_anterior,abono.abono,abono.por_pagar,abono.cuenta.documento.cliente.nombres_apellidos)
        messages.add_message(request, messages.SUCCESS, 'El Abono se registro Correctamente..!')
    return HttpResponseRedirect("/counts/?id=%s"%cuenta.id)

def recibo(request):
    contexto={
        'cuenta':DetalleCuentasCobrar.objects.get(id=request.GET.get('id')),
    }
    return render_to_pdf('recibo.html',contexto)


