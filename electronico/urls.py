from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from Facturacion.views import *
from Inicio.views import index, LoginView, LogoutView
from OrdenesTrabajo.views import ordenes_trabajo
from Personas.views import clientes, buscar_cliente
from Productos.views import registro_productos
from api.url import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('login/',LoginView,name='login'),
    path('logout/',LogoutView,name='logout'),

    path('product/',registro_productos, name='productos'),

    path('client/',clientes, name='clientes'),
    path('search_client/',buscar_cliente, name='buscar_clientes'),

    path('orden_trabajo/',ordenes_trabajo,name='orden_trabajo'),

    path('fact/',facturacion, name='facturacion'),
    path('fac/list/',facturas,name='listaFacturas'),
    path('save_fact/',registroFactura, name='registroFactura'),
    path('fac/details/',registroDetalles,name='registroDetalles'),
    path('fac/signed/',firmar_documento,name='firmar'),
    path('fac/ride/',ride,name='ride'),

    path('counts/',cuentasCobrar,name='cuentasCobrar'),
    path('register/counts/<int:id>/',registar_cuenta),
    path('counts/abono/',registarAbono,name='abono'),
    path('recibe/',recibo,name='recibo'),

    path('envelop_sri/',enviar_sri,name="enviar_sri"),
    path('consulta/',consulta_comprobantes),

    #api
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),


]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
