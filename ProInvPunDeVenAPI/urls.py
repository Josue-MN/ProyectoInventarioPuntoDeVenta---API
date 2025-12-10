from django.urls import path, include
from ProInvPunDeVenAPI.views import *
from rest_framework.routers import DefaultRouter #IMPORTA AUTOMATICAMENTE LAS RUTAS GET,PUT,DELETE,UPDATE
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView #IMPORTA LAS RUTAS PARA EL USO DE TOKENS
from drf_yasg.views import get_schema_view ##GENERA LA DOCUMENTACION MEDIANTE LAS VISTAS YA CREADAS
from drf_yasg import openapi ##IMPORTA LA ESTRUCTURA DE OPENAPI
from rest_framework import permissions ##SE IMPORTA PARA DECIDIR A QUIEN SE LE DARA PERMISO PARA VER LA DOCUMENTACION

router = DefaultRouter() ##CONFIGURA LA CREACION DEL ROUTER, PARA LUEGO DEFINIR TODAS LAS VISTAS AUTOMATICAS CON ROUTERS Y HACER
##MAS AUTOMATICA LA GESTION DE GET,UPDATE,DELETE Y PUT
router.register('bodegas', BodegasViewSets)
router.register('cargos', CargosViewSets)
router.register('categoriaProducto', CategoriaProductoViewSets)
router.register('empleados', EmpleadosViewSets)
router.register('productos', ProductosViewSets)
router.register('usuarios', UsuariosViewSets)

##SCHEMA_VIEW GENERA LA INTERFAZ GRAFICA PARA SER USADA
schema_view = get_schema_view(
    openapi.Info(
        title="API PROYECTO INVENTARIO", #NOMBRE API
        default_version="v1", #VERSION QUE SE UTILIZARA
        description="Documentacion automatica generada por swagger", #DESCRIPCION
        terms_of_service="https://www.google.com/policies/terms/", #TERMINOS DE SERVICIO
        contact=openapi.Contact(email="contact@snippets.local"), #CONTACTO
        license=openapi.License(name="BSD License"), #LICENCIA
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    ##OBTIENE LOS TOKEN ACCESS Y REFRESH (USERNAME Y PASSWORD)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    ##RUTA QUE RENUEVA EL ACCESO DADO AL USUARIO, CON ACCESO O DENEGADO
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', logoutView.as_view(), name="token_logout"),
    ##CREA LA RUTA SWAGGER SEGUN, ESPECICANDO SEGUN LA INTERFAZ CREADA SCHEMA_VIEW QUE SE QUIERE USAR
    ##LA INTERFAZ GRAFICA WITH_UI DE SWAGGER, Y QUE NO TNEGA TIEMPO PARA GENERAR CACHE Y ASI GENERAR QUE SE ACTUALICE
    ##TODOO EL TIEMPO
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
    ##CREA LA RUTA REDOC SEGUN, ESPECICANDO SEGUN LA INTERFAZ CREADA SCHEMA_VIEW QUE SE QUIERE USAR
    ##LA INTERFAZ GRAFICA WITH_UI DE REDOC, Y QUE NO TNEGA TIEMPO PARA GENERAR CACHE Y ASI GENERAR QUE SE ACTUALICE
    ##TODOO EL TIEMPO, GENERANDO UNA INTERFAZ GRAFICA MAS ELEGANTE PARA LA VISTA DE DOCUMENTACION
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),
    ##AGREGA TODAS LAS RUTAS CREADAS CON ROUTER
    path('', include(router.urls)),
]