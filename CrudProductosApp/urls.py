# Importaciones necesarias
from django.urls import path  # Función para definir rutas URL
from CrudProductosApp import views  # Importa las vistas de la app CrudProductosApp

# ========================================================================
# Lista de rutas URL de la aplicación CrudProductosApp
# ========================================================================
# Lista de rutas (URL patterns) de la aplicación CRUD de producto solo para otros usuarios.
urlpatterns = [
    
    path('crud-productos/', views.productosData, name='crud-producto'),

    path('crud-productos/registro-producto/', views.productosRegistrationView, name='registrar-producto'),
    
    path('crud-productos/detalle-producto/<int:IdProducto>', views.detalleProducto, name='detalle-producto'),

    path('crud-productos/actualizar-producto/<int:IdProducto>', views.actualizarProducto, name='actualizar-producto'),

    path('crud-productos/confirmar-eliminar/<int:IdProducto>', views.confirmarEliminar, name='confirmar-eliminar-producto'),

    path('crud-productos/eliminar-producto/<int:IdProducto>', views.eliminarProducto, name='eliminar-producto'),

]
