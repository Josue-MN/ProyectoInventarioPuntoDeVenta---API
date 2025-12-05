from django.urls import path, include
from ProInvPunDeVenAPI.views import *
from rest_framework.routers import DefaultRouter #IMPORTA AUTOMATICAMENTE LAS RUTAS GET,PUT,DELETE,UPDATE
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView #IMPORTA LAS RUTAS PARA EL USO DE TOKENS

router = DefaultRouter() ##CONFIGURA LA CREACION DEL ROUTER, PARA LUEGO DEFINIR TODAS LAS VISTAS AUTOMATICAS CON ROUTERS Y HACER
##MAS AUTOMATICA LA GESTION DE GET,UPDATE,DELETE Y PUT
router.register('bodegas', BodegasViewSets)
router.register('cargos', CargosViewSets)
router.register('categoriaProducto', CategoriaProductoViewSets)
router.register('empleados', EmpleadosViewSets)
router.register('productos', ProductosViewSets)
router.register('usuarios', UsuariosViewSets)

urlpatterns = [
    ##OBTIENE LOS TOKEN ACCESS Y REFRESH (USERNAME Y PASSWORD)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtein_pair'),
    ##RUTA QUE RENUEVA EL ACCESO DADO AL USUARIO, CON ACCESO O DENEGADO
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ##AGREGA TODAS LAS RUTAS CREADAS CON ROUTER
    path('', include(router.urls)),
]