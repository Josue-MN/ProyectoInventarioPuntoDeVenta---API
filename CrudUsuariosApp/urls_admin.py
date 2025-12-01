from django.urls import path
from CrudUsuariosApp import views

# Lista de rutas para la aplicación CrudUsuariosApp solo par admin
urlpatterns = [

    path('crud-usuarios/', views.usuariosData, name='admin-crud-usuario'),

    path('crud-usuarios/registro-usuario/', views.usuariosRegistrationView, name='admin-registrar-usuario'),

    path('crud-usuarios/detalle-usuario/<int:IdUsuarios>', views.detalleUsuario, name='admin-detalle-usuario'),

    path('crud-usuarios/actualizar-usuario/<int:IdUsuarios>', views.actualizarUsuario, name='admin-actualizar-usuario'),

    path('crud-usuarios/confirmar-eliminar/<int:IdUsuarios>', views.confirmarEliminar, name='admin-confirmar-eliminar-usuario'),

    path('crud-usuarios/eliminar-usuario/<int:IdUsuarios>/', views.eliminarUsuario, name='admin-eliminar-usuario'),

]
