from django.urls import path
from CrudBodegasApp import views


# Lista de rutas (URL patterns) de la aplicación CRUD de bodegas solo par admin.
urlpatterns = [

    # -------------------------------------------------------------------------
    # LISTADO DE BODEGAS
    # -------------------------------------------------------------------------
    # Muestra la tabla/lista con todas las bodegas registradas.
    path(
        'crud-bodegas/',                # URL del listado principal
        views.bodegasData,              # Vista que muestra todas las bodegas
        name='admin-crud-bodega'        # Nombre único de la ruta
    ),

    # -------------------------------------------------------------------------
    # REGISTRO DE BODEGA
    # -------------------------------------------------------------------------
    # Muestra el formulario para registrar una nueva bodega.
    path(
        'crud-bodegas/registro-bodega/',    # URL del formulario de registro
        views.bodegasRegistracionView,      # Vista que procesa el registro
        name='admin-registrar-bodega'       # Nombre de la ruta
    ),

    # -------------------------------------------------------------------------
    # DETALLE DE UNA BODEGA ESPECÍFICA
    # -------------------------------------------------------------------------
    # Muestra información completa de una bodega seleccionada.
    path(
        'crud-bodegas/detalle-bodega/<int:IdBodega>',  # ID dinámico pasado por la URL
        views.detalleBodega,                           # Vista que obtiene el detalle
        name='admin-detalle-bodega'                    # Nombre de esta ruta
    ),

    # -------------------------------------------------------------------------
    # ACTUALIZAR UNA BODEGA
    # -------------------------------------------------------------------------
    # Muestra y procesa el formulario para actualizar una bodega existente.
    path(
        'crud-bodegas/actualizar-bodega/<int:IdBodega>',  # ID de la bodega a editar
        views.actualizarBodega,                           # Vista encargada de actualizar
        name='admin-actualizar-bodega'                    # Nombre único
    ),

    # -------------------------------------------------------------------------
    # PANTALLA DE CONFIRMACIÓN DE ELIMINACIÓN
    # -------------------------------------------------------------------------
    # Muestra una pantalla donde el usuario confirma si desea eliminar la bodega.
    path(
        'crud-bodegas/confirmar-eliminar/<int:IdBodega>',  # ID de la bodega a eliminar
        views.confirmarEliminar,                           # Vista de confirmación
        name='admin-confirmar-eliminar-bodega'             # Nombre de la ruta
    ),

    # -------------------------------------------------------------------------
    # ELIMINACIÓN DEFINITIVA
    # -------------------------------------------------------------------------
    # Ejecuta la acción de eliminar la bodega de la base de datos.
    path(
        'crud-bodegas/eliminar-bodega/<int:IdBodega>', # ID de la bodega a eliminar
        views.eliminarBodega,                          # Vista que realiza la eliminación
        name='admin-eliminar-bodega'                   # Nombre único de esta ruta
    ),
]
