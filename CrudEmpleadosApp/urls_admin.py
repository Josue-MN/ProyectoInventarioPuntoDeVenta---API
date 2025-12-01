from django.urls import path       # Función para definir rutas URL
from CrudEmpleadosApp import views  # Importa las vistas definidas en la app CrudEmpleadosApp

# ========================================================================
# Lista de rutas URL de la aplicación CrudEmpleadosApp para admin
# ========================================================================
urlpatterns = [

    path('crud-empleado/', views.empleadosData, name='admin-crud-empleado'),

    path('crud-empleado/registro-empleado/', views.empleadoRegistrationView, name='admin-registrar-empleado'),

    path('crud-empleado/detalle-empleado/<int:IdEmpleado>', views.detalleEmpleado, name='admin-detalle-empleado'),

    path('crud-empleado/actualizar-empleado/<int:IdEmpleado>', views.actualizarEmpleado, name='admin-actualizar-empleado'),

    path('crud-empleado/confirmar-eliminar/<int:IdEmpleado>', views.confirmarEliminar, name='admin-confirmar-eliminar-empleado'),

    path('crud-empleado/eliminar-empleado/<int:IdEmpleado>', views.eliminarEmpleado, name='admin-eliminar-empleado'),
    
]
