# CrudProductosApp/urls_admin.py

from django.urls import path
from CrudProductosApp import views

# Lista de rutas (URL patterns) de la aplicación CRUD de producto solo para admin.
urlpatterns = [
    # Lista de productos para Administrador
    path('crud-productos/', views.productosData, name='admin-crud-producto'),

    # Registrar producto (admin)
    path('crud-productos/registro-producto/', views.productosRegistrationView, name='admin-registrar-producto'),

    # Actualizar producto (admin)
    path('crud-productos/actualizar-producto/<int:IdProducto>', views.actualizarProducto, name='admin-actualizar-producto'),

    # Eliminar producto (admin)
    path('crud-productos/eliminar-producto/<int:IdProducto>', views.eliminarProducto, name='admin-eliminar-producto'),

    # Confirmar eliminación (admin)
    path('crud-productos/confirmar-eliminar/<int:IdProducto>', views.confirmarEliminar, name='admin-confirmar-eliminar-producto'),

    # Detalle producto (admin)
    path('crud-productos/detalle-producto/<int:IdProducto>', views.detalleProducto, name='admin-detalle-producto'),
]
