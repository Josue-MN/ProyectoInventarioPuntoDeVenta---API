# IMPORTACIONES NECESARIAS

# Importa las herramientas del panel de administración de Django.
from django.contrib import admin

# Importa todos los modelos de auditoría que se registrarán en el admin.
from .models import (
    AuditoriaBodega,
    AuditoriaCargo,
    AuditoriaCategoria,
    AuditoriaEmpleado,
    AuditoriaProducto,
    AuditoriaUsuario
)


# =============================================================================
# ADMIN BASE SOLO LECTURA
# Clase genérica usada como base para todas las auditorías.
# Esta clase deshabilita agregar, editar y eliminar registros.
# Se utiliza para que las auditorías sean 100% históricas y no modificables.
# =============================================================================
class AuditoriaBaseAdmin(admin.ModelAdmin):

    # ------------------------------
    # Bloquea la opción de "Agregar"
    # ------------------------------
    def has_add_permission(self, request):
        return False

    # ------------------------------
    # Bloquea la opción de "Modificar"
    # obj = instancia del modelo (opcional)
    # ------------------------------
    def has_change_permission(self, request, obj=None):
        return False

    # ------------------------------
    # Bloquea la opción de "Eliminar"
    # ------------------------------
    def has_delete_permission(self, request, obj=None):
        return False

    # -------------------------------------------------
    # Elimina las acciones masivas del admin (por ejemplo,
    # "Eliminar seleccionados"). Esto asegura que nada pueda
    # ser borrado aunque existan opciones en la interfaz.
    # -------------------------------------------------
    actions = None

    # Cantidad de elementos por página en la vista de lista.
    list_per_page = 10


# =============================================================================
# AUDITORÍA BODEGA
# Administrador del modelo AuditoriaBodega
# =============================================================================
class AuditoriaBodegaAdmin(AuditoriaBaseAdmin):

    # Campos que se mostrarán en la tabla principal del admin
    list_display = [
        "IdAuditoriaBodega",
        "Accion",
        "BodegaIdRespaldo",
        "BodegaNombreRespaldo",
        "Fecha_hora",
    ]

    # Filtros en la barra lateral derecha
    list_filter = ["Accion", "Fecha_hora"]

    # Campos que se podrán buscar desde el buscador del admin
    search_fields = [
        "IdAuditoriaBodega",
        "Accion",
        "BodegaIdRespaldo",
        "BodegaNombreRespaldo",
    ]

    # Organización de los campos dentro del detalles de un registro
    fieldsets = (
        ('Datos importantes', {
            'fields': ('Accion', 'Fecha_hora')
        }),
        ('Asociados', {
            'fields': ('Bodega', 'Usuario')
        }),
        ('Respaldo', {
            'fields': ('BodegaIdRespaldo', 'BodegaNombreRespaldo')
        }),
    )

    # Campos que no se pueden modificar en el formulario del admin
    readonly_fields = [
        'IdAuditoriaBodega',
        'Bodega',
        'Usuario',
        'BodegaIdRespaldo',
        'BodegaNombreRespaldo',
        'Accion',
        'Fecha_hora',
    ]


# =============================================================================
# AUDITORÍA CARGO
# =============================================================================
class AuditoriaCargoAdmin(AuditoriaBaseAdmin):

    list_display = [
        "IdAuditoriaCargo",
        "Accion",
        "CargoIdRespaldo",
        "CargoNombreRespaldo",
        "Fecha_hora",
    ]

    list_filter = ["Accion", "Fecha_hora"]

    search_fields = [
        "IdAuditoriaCargo",
        "Accion",
        "CargoIdRespaldo",
        "CargoNombreRespaldo",
    ]

    fieldsets = (
        ('Datos importantes', {
            'fields': ('Accion', 'Fecha_hora')
        }),
        ('Asociados', {
            'fields': ('Cargo', 'Usuario')
        }),
        ('Respaldo', {
            'fields': ('CargoIdRespaldo', 'CargoNombreRespaldo')
        }),
    )

    readonly_fields = [
        'IdAuditoriaCargo',
        'Cargo',
        'Usuario',
        'CargoIdRespaldo',
        'CargoNombreRespaldo',
        'Accion',
        'Fecha_hora',
    ]


# =============================================================================
# AUDITORÍA CATEGORÍA
# =============================================================================
class AuditoriaCategoriaAdmin(AuditoriaBaseAdmin):

    list_display = [
        "IdAuditoriaCategoria",
        "Accion",
        "CategoriaIdRespaldo",
        "CategoriaNombreRespaldo",
        "Fecha_hora",
    ]

    list_filter = ["Accion", "Fecha_hora"]

    search_fields = [
        "IdAuditoriaCategoria",
        "Accion",
        "CategoriaIdRespaldo",
        "CategoriaNombreRespaldo",
    ]

    fieldsets = (
        ('Datos importantes', {
            'fields': ('Accion', 'Fecha_hora')
        }),
        ('Asociados', {
            'fields': ('Categoria', 'Usuario')
        }),
        ('Respaldo', {
            'fields': ('CategoriaIdRespaldo', 'CategoriaNombreRespaldo')
        }),
    )

    readonly_fields = [
        'IdAuditoriaCategoria',
        'Categoria',
        'Usuario',
        'CategoriaIdRespaldo',
        'CategoriaNombreRespaldo',
        'Accion',
        'Fecha_hora',
    ]


# =============================================================================
# AUDITORÍA EMPLEADO
# =============================================================================
class AuditoriaEmpleadoAdmin(AuditoriaBaseAdmin):

    list_display = [
        "IdAuditoriaEmpleado",
        "Accion",
        "EmpleadoIdRespaldo",
        "EmpleadoNombreRespaldo",
        "Fecha_hora",
    ]

    list_filter = ["Accion", "Fecha_hora"]

    search_fields = [
        "IdAuditoriaEmpleado",
        "Accion",
        "EmpleadoIdRespaldo",
        "EmpleadoNombreRespaldo",
    ]

    fieldsets = (
        ('Datos importantes', {
            'fields': ('Accion', 'Fecha_hora')
        }),
        ('Asociados', {
            'fields': ('Empleado', 'Usuario')
        }),
        ('Respaldo', {
            'fields': ('EmpleadoIdRespaldo', 'EmpleadoNombreRespaldo')
        }),
    )

    readonly_fields = [
        'IdAuditoriaEmpleado',
        'Empleado',
        'Usuario',
        'EmpleadoIdRespaldo',
        'EmpleadoNombreRespaldo',
        'Accion',
        'Fecha_hora',
    ]


# =============================================================================
# AUDITORÍA PRODUCTO
# =============================================================================
class AuditoriaProductoAdmin(AuditoriaBaseAdmin):

    list_display = [
        "IdAuditoriaProducto",
        "Accion",
        "ProductoIdRespaldo",
        "ProductoNombreRespaldo",
        "Fecha_hora",
    ]

    list_filter = ["Accion", "Fecha_hora"]

    search_fields = [
        "IdAuditoriaProducto",
        "Accion",
        "ProductoIdRespaldo",
        "ProductoNombreRespaldo",
    ]

    fieldsets = (
        ('Datos importantes', {
            'fields': ('Accion', 'Fecha_hora')
        }),
        ('Asociados', {
            'fields': ('Producto', 'Usuario')
        }),
        ('Respaldo', {
            'fields': ('ProductoIdRespaldo', 'ProductoNombreRespaldo')
        }),
    )

    readonly_fields = [
        'IdAuditoriaProducto',
        'Producto',
        'Usuario',
        'ProductoIdRespaldo',
        'ProductoNombreRespaldo',
        'Accion',
        'Fecha_hora',
    ]


# =============================================================================
# AUDITORÍA USUARIO
# =============================================================================
class AuditoriaUsuarioAdmin(AuditoriaBaseAdmin):

    list_display = [
        "IdAuditoriaUsuario",
        "Accion",
        "UsuarioIdRespaldo",
        "UsuarioNombreRespaldo",
        "Fecha_hora",
    ]

    list_filter = ["Accion", "Fecha_hora"]

    search_fields = [
        "IdAuditoriaUsuario",
        "Accion",
        "UsuarioIdRespaldo",
        "UsuarioNombreRespaldo",
    ]

    fieldsets = (
        ('Datos importantes', {
            'fields': ('Accion', 'Fecha_hora')
        }),
        ('Asociados', {
            'fields': ('Usuario',)
        }),
        ('Respaldo', {
            'fields': ('UsuarioIdRespaldo', 'UsuarioNombreRespaldo')
        }),
    )

    readonly_fields = [
        'IdAuditoriaUsuario',
        'Usuario',
        'UsuarioIdRespaldo',
        'UsuarioNombreRespaldo',
        'Accion',
        'Fecha_hora',
    ]


# =============================================================================
# REGISTRO DE MODELOS EN EL ADMIN
# Aquí Django conecta cada modelo con su configuración admin.
# =============================================================================
admin.site.register(AuditoriaBodega, AuditoriaBodegaAdmin)
admin.site.register(AuditoriaCargo, AuditoriaCargoAdmin)
admin.site.register(AuditoriaCategoria, AuditoriaCategoriaAdmin)
admin.site.register(AuditoriaEmpleado, AuditoriaEmpleadoAdmin)
admin.site.register(AuditoriaProducto, AuditoriaProductoAdmin)
admin.site.register(AuditoriaUsuario, AuditoriaUsuarioAdmin)
