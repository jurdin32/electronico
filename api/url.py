from rest_framework import routers

from api.Empresa.viewSet import *
from api.Personas.viewSet import *

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('cliente', ClienteViewSet)
router.register('empresa', EmpresaViewSet)