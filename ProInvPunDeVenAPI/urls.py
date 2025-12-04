from django.urls import path, include
from ProInvPunDeVenAPI.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('bodegas', BodegasViewSets)
router.register('cargos', CargosViewSets)
router.register('categoriaProducto', CategoriaProductoViewSets)
router.register('empleados', EmpleadosViewSets)
router.register('productos', ProductosViewSets)
router.register('usuarios', UsuariosViewSets)

urlpatterns = [
    path('', include(router.urls)),
]