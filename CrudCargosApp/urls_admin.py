from django.urls import path
from CrudCargosApp import views

# Lista de rutas para la aplicación CrudCargoApp
urlpatterns = [

    # -------------------------------------------------------------------------
    # LISTAR TODOS LOS CARGOS
    # -------------------------------------------------------------------------
    # Muestra la vista principal del CRUD donde aparece el listado
    # completo de todos los cargos registrados.
    path(
        'crud-cargos/', views.cargosData, name='admin-crud-cargo'
    ),

    # -------------------------------------------------------------------------
    # REGISTRAR UN NUEVO CARGO
    # -------------------------------------------------------------------------
    # Vista encargada de mostrar el formulario de registro
    # y procesar los datos enviados para crear un nuevo cargo.
    path(
        'crud-cargos/registro-cargo/', views.cargosRegistracionView, name='admin-registrar-cargo'
    ),

    # -------------------------------------------------------------------------
    # DETALLE DE UN CARGO ESPECÍFICO
    # -------------------------------------------------------------------------
    # Muestra la información completa de un cargo seleccionado.
    # El parámetro <int:IdCargos> captura el ID del cargo desde la URL.
    path(
        'crud-cargos/detalle-cargo/<int:IdCargos>', views.detalleCargo, name='admin-detalle-cargo'
    ),

    # -------------------------------------------------------------------------
    # ACTUALIZAR UN CARGO
    # -------------------------------------------------------------------------
    # Permite visualizar el formulario precargado con los datos actuales
    # del cargo para luego actualizarlo.
    path(
        'crud-cargos/actualizar-cargo/<int:IdCargos>', views.actualizarCargo, name='admin-actualizar-cargo'
    ),

    # -------------------------------------------------------------------------
    # CONFIRMACIÓN DE ELIMINACIÓN
    # -------------------------------------------------------------------------
    # Muestra una vista de confirmación antes de eliminar definitivamente
    # un cargo, evitando eliminaciones accidentales.
    path(
        'crud-cargos/confirmar-eliminar/<int:IdCargos>', views.confirmarEliminar, name='admin-confirmar-eliminar-cargo'
    ),

    # -------------------------------------------------------------------------
    # ELIMINAR UN CARGO
    # -------------------------------------------------------------------------
    # Ejecuta la eliminación definitiva del cargo usando su ID.
    path(
        'crud-cargos/eliminar-cargo/<int:IdCargos>', views.eliminarCargo, name='admin-eliminar-cargo'
    ),

]

