from django.contrib import admin
from ProInvPunDeVenAPI.models import *

# Register your models here.
# Register your models here.
class BodegaAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista principal del admin
    list_display = [
        "IdBodega",
        "NombreBodega", 
        "UbicacionBodega",
        "EstadoBodega",
        "ObservacionesBodega"]
    # Campos por los cuales se puede filtrar en la barra lateral
    list_filter = [
        "NombreBodega", 
        "UbicacionBodega",
        "EstadoBodega"]
    # Campos que se pueden buscar en la barra de búsqueda del admin
    search_fields = [
        "IdBodega",
        "NombreBodega", 
        "UbicacionBodega",
        "EstadoBodega"]
    # Número de registros a mostrar por página en la lista del admin
    list_per_page = 10

    # Organizamos los campos del formulario en secciones lógicas (informacion basica/informacion secundaria))
    fieldsets = (
        ('Datos importantes', {
            'fields': ('NombreBodega','EstadoBodega')
        }),
        ('A detalle', {
            'fields': ('UbicacionBodega', 'ObservacionesBodega')
        })
    )

    # Definimos los campos que serán solo lectura en el admin y qu eno se pueden editar
    readonly_fields = ['IdBodega']
    
    #Llama al archivo js para la personalizacion de mensajes de guardado segun django admin
    class Media:
        js = ('js/confirmarGuardados.js',)

    # -------------------------------------------------------------
    # Método: save_model
    # Se ejecuta automáticamente al guardar un registro.
    # Permite detectar si se trata de una creación o una actualización
    # y mostrar mensajes personalizados al usuario.
    #
    # Parámetros:
    #   request -> objeto HTTP con la información del usuario actual.
    #   obj -> instancia del modelo que se está guardando.
    #   form -> formulario con los datos validados.
    #   change -> booleano que indica si el registro es nuevo (False)
    #             o está siendo editado (True).
    # -------------------------------------------------------------
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        if not change:
            # Si el registro es nuevo, muestra mensaje de creación
            self.message_user(request, f"La Bodega '{obj.NombreBodega}' se ha creado.")
        if change:
            # Si el registro ya existía, muestra mensaje de actualización
            self.message_user(request, f"La Bodega '{obj.NombreBodega}' se ha actualizado.")

    # -------------------------------------------------------------
    # Método: delete_model
    # Se ejecuta cuando se elimina un único registro desde la vista
    # de detalle del modelo en el administrador.
    #
    # Parámetros:
    #   request -> objeto HTTP actual.
    #   obj -> instancia del modelo que se está eliminando.
    #
    # Flujo:
    #   1. Obtiene el nombre (si existe).
    #   2. Llama al método original de eliminación.
    #   3. Muestra un mensaje de confirmación.
    # -------------------------------------------------------------
    def delete_model(self, request, obj):
        NombreBodega = getattr(obj, 'NombreBodega', str(obj))  # usa nombre si existe, o el objeto
        super().delete_model(request, obj)
        self.message_user(request, f"La Bodega '{NombreBodega}' se ha eliminado.")

    # -------------------------------------------------------------
    # Método: delete_queryset
    # Se ejecuta cuando el usuario elimina varios registros a la vez
    # desde la lista del panel de administración (“Eliminar seleccionados”).
    #
    # Parámetros:
    #   request -> solicitud actual.
    #   queryset -> conjunto de registros seleccionados.
    #
    # Flujo:
    #   1. Cuenta cuántos registros se eliminarán.
    #   2. Llama al método base para eliminarlos.
    #   3. Muestra un mensaje con la cantidad de eliminados.
    # -------------------------------------------------------------
    def delete_queryset(self, request, queryset):
        count = queryset.count()
        super().delete_queryset(request, queryset)
        self.message_user(request, f"Se han eliminado {count} Bodegas correctamente.")

# ========================================================================
# Registro del modelo en el panel de administración
# ========================================================================
# Esto permite que podamos gestionar los registros directamente
# desde el panel de administración de Django (crear, leer, actualizar y eliminar)
admin.site.register(Bodegas, BodegaAdmin)

class CargoAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista principal del admin
    list_display = [
        "IdCargos",
        "TipoDeCargo", 
        "EstadoDelCargo",
        "DescripcionDelCargo",
        "SueldoBase"]
    # Campos por los cuales se puede filtrar en la barra lateral
    list_filter = [
        "TipoDeCargo", 
        "EstadoDelCargo",
        "SueldoBase"]
    # Campos que se pueden buscar en la barra de búsqueda del admin
    search_fields = [
        "IdCargos",
        "TipoDeCargo", 
        "EstadoDelCargo",
        "SueldoBase"]
    # Número de registros a mostrar por página en la lista del admin
    list_per_page = 10

    # Organizamos los campos del formulario en secciones lógicas (informacion basica/informacion secundaria))
    fieldsets = (
        ('Datos importantes', {
            'fields': ('TipoDeCargo','EstadoDelCargo')
        }),
        ('A detalle', {
            'fields': ('DescripcionDelCargo', 'SueldoBase')
        })
    )

    # Definimos los campos que serán solo lectura en el admin y qu eno se pueden editar
    readonly_fields = ['IdCargos']
    
    #Llama al archivo js para la personalizacion de mensajes de guardado segun django admin
    class Media:
        js = ('js/confirmarGuardados.js',)


    # -------------------------------------------------------------
    # Método: save_model
    # Se ejecuta automáticamente al guardar un registro.
    # Permite detectar si se trata de una creación o una actualización
    # y mostrar mensajes personalizados al usuario.
    #
    # Parámetros:
    #   request -> objeto HTTP con la información del usuario actual.
    #   obj -> instancia del modelo que se está guardando.
    #   form -> formulario con los datos validados.
    #   change -> booleano que indica si el registro es nuevo (False)
    #             o está siendo editado (True).
    # -------------------------------------------------------------
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        if not change:
            # Si el registro es nuevo, muestra mensaje de creación
            self.message_user(request, f"El Cargo '{obj.TipoDeCargo}' se ha creado.")
        if change:
            # Si el registro ya existía, muestra mensaje de actualización
            self.message_user(request, f"El Cargo '{obj.TipoDeCargo}' se ha actualizado.")

    # -------------------------------------------------------------
    # Método: delete_model
    # Se ejecuta cuando se elimina un único registro desde la vista
    # de detalle del modelo en el administrador.
    #
    # Parámetros:
    #   request -> objeto HTTP actual.
    #   obj -> instancia del modelo que se está eliminando.
    #
    # Flujo:
    #   1. Obtiene el nombre (si existe).
    #   2. Llama al método original de eliminación.
    #   3. Muestra un mensaje de confirmación.
    # -------------------------------------------------------------
    def delete_model(self, request, obj):
        TipoDeCargo = getattr(obj, 'TipoDeCargo', str(obj))  # usa nombre si existe, o el objeto
        super().delete_model(request, obj)
        self.message_user(request, f"El Cargo '{TipoDeCargo}' se ha eliminado.")

    # -------------------------------------------------------------
    # Método: delete_queryset
    # Se ejecuta cuando el usuario elimina varios registros a la vez
    # desde la lista del panel de administración (“Eliminar seleccionados”).
    #
    # Parámetros:
    #   request -> solicitud actual.
    #   queryset -> conjunto de registros seleccionados.
    #
    # Flujo:
    #   1. Cuenta cuántos registros se eliminarán.
    #   2. Llama al método base para eliminarlos.
    #   3. Muestra un mensaje con la cantidad de eliminados.
    # -------------------------------------------------------------
    def delete_queryset(self, request, queryset):
        count = queryset.count()
        super().delete_queryset(request, queryset)
        self.message_user(request, f"Se han eliminado {count} Cargos correctamente.")

# ========================================================================
# Registro del modelo en el panel de administración
# ========================================================================
# Esto permite que podamos gestionar los registros directamente
# desde el panel de administración de Django (crear, leer, actualizar y eliminar)
admin.site.register(Cargos, CargoAdmin)

class CategoriaProductoAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista principal del admin
    list_display = [
        "IdCategoriaProducto",
        "NombreCategoria", 
        "Descripcion",
        "Estado",
        "Observaciones"]
    # Campos por los cuales se puede filtrar en la barra lateral
    list_filter = [
        "NombreCategoria",
        "Estado"]
    # Campos que se pueden buscar en la barra de búsqueda del admin
    search_fields = [
        "IdCategoriaProducto",
        "NombreCategoria",
        "Estado"]
    # Número de registros a mostrar por página en la lista del admin
    list_per_page = 10

# Organizamos los campos del formulario en secciones lógicas (informacion basica/informacion secundaria))
    fieldsets = (
        ('Datos importantes', {
            'fields': ('NombreCategoria','Estado')
        }),
        ('A detalle', {
            'fields': ('Descripcion', 'Observaciones')
        })
    )

    # Definimos los campos que serán solo lectura en el admin y qu eno se pueden editar
    readonly_fields = ['IdCategoriaProducto']
    
    #Llama al archivo js para la personalizacion de mensajes de guardado segun django admin
    class Media:
        js = ('js/confirmarGuardados.js',)



    # -------------------------------------------------------------
    # Método: save_model
    # Se ejecuta automáticamente al guardar un registro.
    # Permite detectar si se trata de una creación o una actualización
    # y mostrar mensajes personalizados al usuario.
    #
    # Parámetros:
    #   request -> objeto HTTP con la información del usuario actual.
    #   obj -> instancia del modelo que se está guardando.
    #   form -> formulario con los datos validados.
    #   change -> booleano que indica si el registro es nuevo (False)
    #             o está siendo editado (True).
    # -------------------------------------------------------------
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        if not change:
            # Si el registro es nuevo, muestra mensaje de creación
            self.message_user(request, f"La Categoria de Producto '{obj.NombreCategoria}' se ha creado.")
        if change:
            # Si el registro ya existía, muestra mensaje de actualización
            self.message_user(request, f"La Categoria de Producto '{obj.NombreCategoria}' se ha actualizado.")

    # -------------------------------------------------------------
    # Método: delete_model
    # Se ejecuta cuando se elimina un único registro desde la vista
    # de detalle del modelo en el administrador.
    #
    # Parámetros:
    #   request -> objeto HTTP actual.
    #   obj -> instancia del modelo que se está eliminando.
    #
    # Flujo:
    #   1. Obtiene el nombre (si existe).
    #   2. Llama al método original de eliminación.
    #   3. Muestra un mensaje de confirmación.
    # -------------------------------------------------------------
    def delete_model(self, request, obj):
        NombreCategoria = getattr(obj, 'NombreCategoria', str(obj))  # usa nombre si existe, o el objeto
        super().delete_model(request, obj)
        self.message_user(request, f"La Categoria de Producto '{NombreCategoria}' se ha eliminado.")

    # -------------------------------------------------------------
    # Método: delete_queryset
    # Se ejecuta cuando el usuario elimina varios registros a la vez
    # desde la lista del panel de administración (“Eliminar seleccionados”).
    #
    # Parámetros:
    #   request -> solicitud actual.
    #   queryset -> conjunto de registros seleccionados.
    #
    # Flujo:
    #   1. Cuenta cuántos registros se eliminarán.
    #   2. Llama al método base para eliminarlos.
    #   3. Muestra un mensaje con la cantidad de eliminados.
    # -------------------------------------------------------------
    def delete_queryset(self, request, queryset):
        count = queryset.count()
        super().delete_queryset(request, queryset)
        self.message_user(request, f"Se han eliminado {count} Categorias de Productos correctamente.")

# ========================================================================
# Registro del modelo en el panel de administración
# ========================================================================
# Esto permite que podamos gestionar los registros directamente
# desde el panel de administración de Django (crear, leer, actualizar y eliminar)
admin.site.register(CategoriaProducto, CategoriaProductoAdmin)

class EmpleadoAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista principal del admin
    list_display = [
        "IdEmpleado",
        "RutEmpleado", 
        "NombreEmpleado",
        "ApellidoEmpleado",
        "EdadEmpleado",
        "NumeroTelefonoEmpleado"]
    # Campos por los cuales se puede filtrar en la barra lateral
    list_filter = [
        "RutEmpleado", 
        "NombreEmpleado",
        "ApellidoEmpleado"]
    # Campos que se pueden buscar en la barra de búsqueda del admin
    search_fields = [
        "IdEmpleado",
        "RutEmpleado", 
        "NombreEmpleado",
        "ApellidoEmpleado"]
    # Número de registros a mostrar por página en la lista del admin
    list_per_page = 10

    # Organizamos los campos del formulario en secciones lógicas (informacion basica/informacion secundaria))
    fieldsets = (
        ('Datos importantes', {
            'fields': ('RutEmpleado','NombreEmpleado','ApellidoEmpleado')
        }),
        ('A detalle', {
            'fields': ('EdadEmpleado', 'NumeroTelefonoEmpleado')
        })
    )

    # Definimos los campos que serán solo lectura en el admin y qu eno se pueden editar
    readonly_fields = ['IdEmpleado']
    
    #Llama al archivo js para la personalizacion de mensajes de guardado segun django admin
    class Media:
        js = ('js/confirmarGuardados.js',)



    # -------------------------------------------------------------
    # Método: save_model
    # Se ejecuta automáticamente al guardar un registro.
    # Permite detectar si se trata de una creación o una actualización
    # y mostrar mensajes personalizados al usuario.
    #
    # Parámetros:
    #   request -> objeto HTTP con la información del usuario actual.
    #   obj -> instancia del modelo que se está guardando.
    #   form -> formulario con los datos validados.
    #   change -> booleano que indica si el registro es nuevo (False)
    #             o está siendo editado (True).
    # -------------------------------------------------------------
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        if not change:
            # Si el registro es nuevo, muestra mensaje de creación
            self.message_user(request, f"El Empleado '{obj.NombreEmpleado}' se ha creado.")
        if change:
            # Si el registro ya existía, muestra mensaje de actualización
            self.message_user(request, f"El Empleado '{obj.NombreEmpleado}' se ha actualizado.")

    # -------------------------------------------------------------
    # Método: delete_model
    # Se ejecuta cuando se elimina un único registro desde la vista
    # de detalle del modelo en el administrador.
    #
    # Parámetros:
    #   request -> objeto HTTP actual.
    #   obj -> instancia del modelo que se está eliminando.
    #
    # Flujo:
    #   1. Obtiene el nombre (si existe).
    #   2. Llama al método original de eliminación.
    #   3. Muestra un mensaje de confirmación.
    # -------------------------------------------------------------
    def delete_model(self, request, obj):
        NombreEmpleado = getattr(obj, 'NombreEmpleado', str(obj))  # usa nombre si existe, o el objeto
        super().delete_model(request, obj)
        self.message_user(request, f"El Empleado '{NombreEmpleado}' se ha eliminado.")

    # -------------------------------------------------------------
    # Método: delete_queryset
    # Se ejecuta cuando el usuario elimina varios registros a la vez
    # desde la lista del panel de administración (“Eliminar seleccionados”).
    #
    # Parámetros:
    #   request -> solicitud actual.
    #   queryset -> conjunto de registros seleccionados.
    #
    # Flujo:
    #   1. Cuenta cuántos registros se eliminarán.
    #   2. Llama al método base para eliminarlos.
    #   3. Muestra un mensaje con la cantidad de eliminados.
    # -------------------------------------------------------------
    def delete_queryset(self, request, queryset):
        count = queryset.count()
        super().delete_queryset(request, queryset)
        self.message_user(request, f"Se han eliminado {count} Empleados correctamente.")

# ========================================================================
# Registro del modelo en el panel de administración
# ========================================================================
# Esto permite que podamos gestionar los registros directamente
# desde el panel de administración de Django (crear, leer, actualizar y eliminar)
admin.site.register(Empleados, EmpleadoAdmin)


class ProductoAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista principal del admin
    list_display = [
        'IdProducto',
        'CodigoDeBarras', 
        'ValorProducto', 
        'StockProducto', 
        'NombreProducto', 
        'MarcaProducto', 
        'FechaDeVencimiento',
        'CategoriaProducto',
        'Bodegas'
    ]
    # Campos por los cuales se puede filtrar en la barra lateral
    list_filter = [ 
        "CodigoDeBarras",
        'ValorProducto', 
        "NombreProducto"]
    # Campos que se pueden buscar en la barra de búsqueda del admin
    search_fields = [
        'IdProducto',
        'CodigoDeBarras',
        'NombreProducto',
        'MarcaProducto', ]
    # Número de registros a mostrar por página en la lista del admin
    list_per_page = 10

# Organizamos los campos del formulario en secciones lógicas (informacion basica/informacion secundaria))
    fieldsets = (
        ('Datos importantes', {
            'fields': ('CodigoDeBarras','ValorProducto','StockProducto')
        }),
        ('A detalle', {
            'fields': ('NombreProducto', 'MarcaProducto','FechaDeVencimiento','CategoriaProducto')
        })
    )

    # Definimos los campos que serán solo lectura en el admin y qu eno se pueden editar
    readonly_fields = ['IdProducto']
    
    #Llama al archivo js para la personalizacion de mensajes de guardado segun django admin
    class Media:
        js = ('js/confirmarGuardados.js',)



    # -------------------------------------------------------------
    # Método: save_model
    # Se ejecuta automáticamente al guardar un registro.
    # Permite detectar si se trata de una creación o una actualización
    # y mostrar mensajes personalizados al usuario.
    #
    # Parámetros:
    #   request -> objeto HTTP con la información del usuario actual.
    #   obj -> instancia del modelo que se está guardando.
    #   form -> formulario con los datos validados.
    #   change -> booleano que indica si el registro es nuevo (False)
    #             o está siendo editado (True).
    # -------------------------------------------------------------
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        if not change:
            # Si el registro es nuevo, muestra mensaje de creación
            self.message_user(request, f"El Producto '{obj.NombreProducto}' se ha creado.")
        if change:
            # Si el registro ya existía, muestra mensaje de actualización
            self.message_user(request, f"El Producto '{obj.NombreProducto}' se ha actualizado.")

    # -------------------------------------------------------------
    # Método: delete_model
    # Se ejecuta cuando se elimina un único registro desde la vista
    # de detalle del modelo en el administrador.
    #
    # Parámetros:
    #   request -> objeto HTTP actual.
    #   obj -> instancia del modelo que se está eliminando.
    #
    # Flujo:
    #   1. Obtiene el nombre (si existe).
    #   2. Llama al método original de eliminación.
    #   3. Muestra un mensaje de confirmación.
    # -------------------------------------------------------------
    def delete_model(self, request, obj):
        NombreProducto = getattr(obj, 'NombreProducto', str(obj))  # usa nombre si existe, o el objeto
        super().delete_model(request, obj)
        self.message_user(request, f"El Producto '{NombreProducto}' se ha eliminado.")

    # -------------------------------------------------------------
    # Método: delete_queryset
    # Se ejecuta cuando el usuario elimina varios registros a la vez
    # desde la lista del panel de administración (“Eliminar seleccionados”).
    #
    # Parámetros:
    #   request -> solicitud actual.
    #   queryset -> conjunto de registros seleccionados.
    #
    # Flujo:
    #   1. Cuenta cuántos registros se eliminarán.
    #   2. Llama al método base para eliminarlos.
    #   3. Muestra un mensaje con la cantidad de eliminados.
    # -------------------------------------------------------------
    def delete_queryset(self, request, queryset):
        count = queryset.count()
        super().delete_queryset(request, queryset)
        self.message_user(request, f"Se han eliminado {count} Productos correctamente.")

# ========================================================================
# Registro del modelo en el panel de administración
# ========================================================================
# Esto permite que podamos gestionar los registros directamente
# desde el panel de administración de Django (crear, leer, actualizar y eliminar)
admin.site.register(Productos, ProductoAdmin)


class UsuarioAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista principal del admin
    list_display = [
        'IdUsuarios',
        'Username',
        'Password',
        'CorreoElectronico',
        'Empleado',
        'Cargo']
    # Campos por los cuales se puede filtrar en la barra lateral
    list_filter = [
        'Username',
        'CorreoElectronico',
        'Cargo']
    # Campos que se pueden buscar en la barra de búsqueda del admin
    search_fields = [
        'IdUsuarios',
        'Username',
        'CorreoElectronico',
        'Empleado',]
    # Número de registros a mostrar por página en la lista del admin
    list_per_page = 10

    
# Organizamos los campos del formulario en secciones lógicas (informacion basica/informacion secundaria))
    fieldsets = (
        ('Datos importantes', {
            'fields': ('Username','Password','ConfirmarPassword')
        }),
        ('A detalle', {
            'fields': ('CorreoElectronico','Empleado','Cargo')
        })
    )

    # Definimos los campos que serán solo lectura en el admin y qu eno se pueden editar
    readonly_fields = ['IdUsuarios']
    
    #Llama al archivo js para la personalizacion de mensajes de guardado segun django admin
    class Media:
        js = ('js/confirmarGuardados.js',)

    # -------------------------------------------------------------
    # Método: save_model
    # Se ejecuta automáticamente al guardar un registro.
    # Permite detectar si se trata de una creación o una actualización
    # y mostrar mensajes personalizados al usuario.
    #
    # Parámetros:
    #   request -> objeto HTTP con la información del usuario actual.
    #   obj -> instancia del modelo que se está guardando.
    #   form -> formulario con los datos validados.
    #   change -> booleano que indica si el registro es nuevo (False)
    #             o está siendo editado (True).
    # -------------------------------------------------------------
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        if not change:
            # Si el registro es nuevo, muestra mensaje de creación
            self.message_user(request, f"El Usuario '{obj.Username}' se ha creado.")
        if change:
            # Si el registro ya existía, muestra mensaje de actualización
            self.message_user(request, f"El Usuario '{obj.Username}' se ha actualizado.")

    # -------------------------------------------------------------
    # Método: delete_model
    # Se ejecuta cuando se elimina un único registro desde la vista
    # de detalle del modelo en el administrador.
    #
    # Parámetros:
    #   request -> objeto HTTP actual.
    #   obj -> instancia del modelo que se está eliminando.
    #
    # Flujo:
    #   1. Obtiene el nombre (si existe).
    #   2. Llama al método original de eliminación.
    #   3. Muestra un mensaje de confirmación.
    # -------------------------------------------------------------
    def delete_model(self, request, obj):
        Username = getattr(obj, 'Username', str(obj))  # usa nombre si existe, o el objeto
        super().delete_model(request, obj)
        self.message_user(request, f"El Usuario '{Username}' se ha eliminado.")

    # -------------------------------------------------------------
    # Método: delete_queryset
    # Se ejecuta cuando el usuario elimina varios registros a la vez
    # desde la lista del panel de administración (“Eliminar seleccionados”).
    #
    # Parámetros:
    #   request -> solicitud actual.
    #   queryset -> conjunto de registros seleccionados.
    #
    # Flujo:
    #   1. Cuenta cuántos registros se eliminarán.
    #   2. Llama al método base para eliminarlos.
    #   3. Muestra un mensaje con la cantidad de eliminados.
    # -------------------------------------------------------------
    def delete_queryset(self, request, queryset):
        count = queryset.count()
        super().delete_queryset(request, queryset)
        self.message_user(request, f"Se han eliminado {count} Usuarios correctamente.")

# ========================================================================
# Registro del modelo en el panel de administración
# ========================================================================
# Esto permite que podamos gestionar los registros directamente
# desde el panel de administración de Django (crear, leer, actualizar y eliminar)
admin.site.register(Usuarios, UsuarioAdmin)



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
