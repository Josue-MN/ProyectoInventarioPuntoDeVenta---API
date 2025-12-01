from django.urls import path
from CrudBodegasApp import views

# Lista de rutas (URL patterns) de la aplicación CRUD de bodegas solo par bodeguero.
urlpatterns = [

    # -------------------------------------------------------------------------
    # LISTAR TODAS LAS BODEGAS
    # -------------------------------------------------------------------------
    # Ruta principal del CRUD de bodegas.
    # Muestra el listado completo de todas las bodegas registradas.
    path(
        'crud-bodegas/',                # URL del listado principal
        views.bodegasData,              # Vista que muestra todas las bodegas
        name='crud-bodega'              # Nombre único de la ruta
    ),

    # -------------------------------------------------------------------------
    # REGISTRAR UNA NUEVA BODEGA
    # -------------------------------------------------------------------------
    # Muestra el formulario para crear una nueva bodega.
    # También procesa el POST si el usuario envía el formulario.
    path(
        'crud-bodegas/registro-bodega/',            # URL del listado principal
        views.bodegasRegistracionView,              # Vista que muestra todas las bodegas
        name='registrar-bodega'                     # Nombre único de la ruta
    ),

    # -------------------------------------------------------------------------
    # DETALLE DE UNA BODEGA ESPECÍFICA
    # -------------------------------------------------------------------------
    # Muestra toda la información de una bodega en particular.
    # <int:IdBodega> captura el ID de la bodega desde la URL.
    path(
        'crud-bodegas/detalle-bodega/<int:IdBodega>',          # URL del listado principal
        views.detalleBodega,                                   # Vista que muestra todas las bodegas
        name='detalle-bodega'                                  # Nombre único de la ruta
    ),

    # -------------------------------------------------------------------------
    # ACTUALIZAR UNA BODEGA
    # -------------------------------------------------------------------------
    # Permite cargar el formulario con los datos actuales de la bodega
    # y luego actualizarla en la base de datos.
    path(
        'crud-bodegas/actualizar-bodega/<int:IdBodega>',    # URL del listado principal
        views.actualizarBodega,                             # Vista que muestra todas las bodegas
        name='actualizar-bodega'                            # Nombre único de la ruta
    ),

    # -------------------------------------------------------------------------
    # CONFIRMACIÓN DE ELIMINACIÓN
    # -------------------------------------------------------------------------
    # Antes de borrar definitivamente una bodega, se muestra una pantalla
    # de advertencia para evitar eliminaciones accidentales.
    path(
        'crud-bodegas/confirmar-eliminar/<int:IdBodega>',   # URL del listado principal
        views.confirmarEliminar,                            # Vista que muestra todas las bodegas
        name='confirmar-eliminar-bodega'                    # Nombre único de la ruta
    ),

    # -------------------------------------------------------------------------
    # ELIMINACIÓN DEFINITIVA DE UNA BODEGA
    # -------------------------------------------------------------------------
    # Ejecuta la acción final de eliminar la bodega indicada por su ID.
    path(
        'crud-bodegas/eliminar-bodega/<int:IdBodega>',      # URL del listado principal
        views.eliminarBodega,                               # Vista que muestra todas las bodegas
        name='eliminar-bodega'                              # Nombre único de la ruta
    ),

]

