from django.db import models # Importación del módulo base de modelos de Django

# Importación de los modelos que serán referenciados mediante claves foráneas
from CrudBodegasApp.models import Bodegas
from CrudUsuariosApp.models import Usuarios
from CrudCargosApp.models import Cargos
from CrudCategoriaProductoApp.models import CategoriaProducto
from CrudEmpleadosApp.models import Empleados
from CrudProductosApp.models import Productos

# Importación para aplicar restricciones únicas en los modelos
from django.db.models import UniqueConstraint

#MANEJO DE AUDITORIAS A BODEGA
class AuditoriaBodega(models.Model):

    # Campo autoincremental que funciona como llave primaria
    IdAuditoriaBodega = models.AutoField(
        primary_key=True,
        db_column='IdAuditoriaBodega'
    )

    # Llave foránea hacia Bodega
    Bodega = models.ForeignKey(
        Bodegas,
        on_delete=models.SET_NULL,
        related_name='auditorias_bodegas',
        db_column="BodegaId",
        null=True,
        blank=True
    )

    # Llave foránea hacia Usuario que realizó la acción
    Usuario = models.ForeignKey(
        Usuarios,
        on_delete=models.SET_NULL, #EVITA QUE AL BORRAR UN USUARIO, SU FK EN LA AUDITORIA QUEDE NULL
        related_name='auditorias_bodega_usuario',
        db_column="UsuarioId",
        null=True,
        blank=True
    )
    
    # Campos de respaldo en caso de que la bodega sea eliminada o modificada
    BodegaIdRespaldo = models.IntegerField(
        null=True,
        blank=True
    )

    # Campos de respaldo en caso de que la bodega sea eliminada o modificada
    BodegaNombreRespaldo = models.CharField(
        max_length=70,
        null=True,
        blank=True
    )

    # Tipo de acción registrada en la auditoría
    Accion = models.CharField(
        max_length=50,
        choices=[
            ('CREAR', 'Crear'),
            ('ACTUALIZAR', 'Actualizar'),
            ('ELIMINAR', 'Eliminar'),
            ('MOVIMIENTO', 'Movimiento de stock')
        ]
    )

    # Tipo de acción registrada en la auditoría
    Fecha_hora = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'AuditoriaBodega'
        constraints = [
            UniqueConstraint(fields=['IdAuditoriaBodega'], name='unique_id_auditoria_bodega'),
        ]

    # Nombre exacto de la tabla en la base de datos
    def __str__(self):
        return f"ID: {self.IdAuditoriaBodega}, Bodega: {self.Bodega}, Nombre Bodega: {self.BodegaNombreRespaldo}, Usuario: {self.Usuario}, Accion: {self.Accion}, Fecha: {self.Fecha_hora}"
    

#-----------------------------------------------------------------------------------------------------------------------------------#
class AuditoriaCargo(models.Model):

    IdAuditoriaCargo = models.AutoField(
        primary_key=True,
        db_column='IdAuditoriaCargo'
    )

    # Llave foránea hacia Bodega
    Cargo = models.ForeignKey(
        Cargos,
        on_delete=models.SET_NULL,
        related_name='auditorias_cargos',
        db_column="CargoId",
        null=True,
        blank=True
    )

    # Llave foránea hacia Usuario que realizó la acción
    Usuario = models.ForeignKey(
        Usuarios,
        on_delete=models.SET_NULL, #EVITA QUE AL BORRAR UN USUARIO, SU FK EN LA AUDITORIA QUEDE NULL
        related_name='auditorias_cargo_usuario',
        db_column="UsuarioId",
        null=True,
        blank=True
    )

    # Datos de respaldo en caso de eliminación
    CargoIdRespaldo = models.IntegerField(
        null=True,
        blank=True
    )
    
    # Datos de respaldo en caso de eliminación
    CargoNombreRespaldo = models.CharField(
        max_length=70,
        null=True,
        blank=True
    )

    # Información de auditoría
    Accion = models.CharField(
        max_length=50,
        choices=[
            ('CREAR', 'Crear'),
            ('ACTUALIZAR', 'Actualizar'),
            ('ELIMINAR', 'Eliminar'),
            ('MOVIMIENTO', 'Movimiento de stock')
        ]
    )

    Fecha_hora = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'AuditoriaCargo'
        constraints = [
            UniqueConstraint(fields=['IdAuditoriaCargo'], name='unique_id_auditoria_cargo'),
        ]


    def __str__(self):
        return f"ID: {self.IdAuditoriaCargo}, Cargo: {self.Cargo}, Nombre Cargo: {self.CargoNombreRespaldo}, Usuario: {self.Usuario}, Accion: {self.Accion}, Fecha: {self.Fecha_hora}"
#-----------------------------------------------------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------------------------------------------------#
class AuditoriaCategoria(models.Model):

    IdAuditoriaCategoria = models.AutoField(
        primary_key=True,
        db_column='IdAuditoriaCategoria'
    )

    # Llave foránea hacia Bodega
    Categoria = models.ForeignKey(
        CategoriaProducto,
        on_delete=models.SET_NULL,
        related_name='auditorias_categoria',
        db_column="CategoriaId",
        null=True,
        blank=True
    )

    # Llave foránea hacia Usuario que realizó la acción
    Usuario = models.ForeignKey(
        Usuarios,
        on_delete=models.SET_NULL, #EVITA QUE AL BORRAR UN USUARIO, SU FK EN LA AUDITORIA QUEDE NULL
        related_name='auditorias_categoria_usuario',
        db_column="UsuarioId",
        null=True,
        blank=True
    )

    CategoriaIdRespaldo = models.IntegerField(
        null=True,
        blank=True
    )

    CategoriaNombreRespaldo = models.CharField(
        max_length=70,
        null=True,
        blank=True
    )

    # Información de auditoría
    Accion = models.CharField(
        max_length=50,
        choices=[
            ('CREAR', 'Crear'),
            ('ACTUALIZAR', 'Actualizar'),
            ('ELIMINAR', 'Eliminar'),
            ('MOVIMIENTO', 'Movimiento de stock')
        ]
    )

    Fecha_hora = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'AuditoriaCategoria'
        constraints = [
            UniqueConstraint(fields=['IdAuditoriaCategoria'], name='unique_id_auditoria_categoria'),
        ]


    def __str__(self):
        return f"ID: {self.IdAuditoriaCategoria}, Categoria: {self.Categoria}, Nombre Categoria: {self.CategoriaNombreRespaldo}, Usuario: {self.Usuario}, Accion: {self.Accion}, Fecha: {self.Fecha_hora}"
#-----------------------------------------------------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------------------------------------------------#
class AuditoriaEmpleado(models.Model):

    IdAuditoriaEmpleado = models.AutoField(
        primary_key=True,
        db_column='IdAuditoriaEmpleado'
    )

    # Llave foránea hacia Bodega
    Empleado = models.ForeignKey(
        Empleados,
        on_delete=models.SET_NULL,
        related_name='auditorias_empleado',
        db_column="EmpleadoId",
        null=True,
        blank=True
    )

    # Llave foránea hacia Usuario que realizó la acción
    Usuario = models.ForeignKey(
        Usuarios,
        on_delete=models.SET_NULL, #EVITA QUE AL BORRAR UN USUARIO, SU FK EN LA AUDITORIA QUEDE NULL
        related_name='auditorias_empleado_usuario',
        db_column="UsuarioId",
        null=True,
        blank=True
    )

    EmpleadoIdRespaldo = models.IntegerField(
        null=True,
        blank=True
    )

    EmpleadoNombreRespaldo = models.CharField(
        max_length=70,
        null=True,
        blank=True
    )

    # Información de auditoría
    Accion = models.CharField(
        max_length=50,
        choices=[
            ('CREAR', 'Crear'),
            ('ACTUALIZAR', 'Actualizar'),
            ('ELIMINAR', 'Eliminar'),
            ('MOVIMIENTO', 'Movimiento de stock')
        ]
    )

    Fecha_hora = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'AuditoriaEmpleado'
        constraints = [
            UniqueConstraint(fields=['IdAuditoriaEmpleado'], name='unique_id_auditoria_empleado'),
        ]


    def __str__(self):
        return f"ID: {self.IdAuditoriaEmpleado}, Empleado: {self.Empleado}, Nombre Empleado: {self.EmpleadoNombreRespaldo}, Usuario: {self.Usuario}, Accion: {self.Accion}, Fecha: {self.Fecha_hora}"
#-----------------------------------------------------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------------------------------------------------#
class AuditoriaProducto(models.Model):

    IdAuditoriaProducto = models.AutoField(
        primary_key=True,
        db_column='IdAuditoriaProducto'
    )

    # Llave foránea hacia Bodega
    Producto = models.ForeignKey(
        Productos,
        on_delete=models.SET_NULL,
        related_name='auditorias_producto',
        db_column="ProductoId",
        null=True,
        blank=True
    )

    # Llave foránea hacia Usuario que realizó la acción
    Usuario = models.ForeignKey(
        Usuarios,
        on_delete=models.SET_NULL, #EVITA QUE AL BORRAR UN USUARIO, SU FK EN LA AUDITORIA QUEDE NULL
        related_name='auditorias_producto_usuario',
        db_column="UsuarioId",
        null=True,
        blank=True
    )

    ProductoIdRespaldo = models.IntegerField(
        null=True,
        blank=True
    )

    ProductoNombreRespaldo = models.CharField(
        max_length=70,
        null=True,
        blank=True
    )

    # Información de auditoría
    Accion = models.CharField(
        max_length=50,
        choices=[
            ('CREAR', 'Crear'),
            ('ACTUALIZAR', 'Actualizar'),
            ('ELIMINAR', 'Eliminar'),
            ('MOVIMIENTO', 'Movimiento de stock')
        ]
    )

    Fecha_hora = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'AuditoriaProducto'
        constraints = [
            UniqueConstraint(fields=['IdAuditoriaProducto'], name='unique_id_auditoria_producto'),
        ]


    def __str__(self):
        return f"ID: {self.IdAuditoriaProducto}, Producto: {self.Producto}, Nombre Producto: {self.ProductoNombreRespaldo}, Usuario: {self.Usuario}, Accion: {self.Accion}, Fecha: {self.Fecha_hora}"
#-----------------------------------------------------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------------------------------------------------#
class AuditoriaUsuario(models.Model):

    IdAuditoriaUsuario = models.AutoField(
        primary_key=True,
        db_column='IdAuditoriaUsuario'
    )

    # Llave foránea hacia Usuario que realizó la acción
    Usuario = models.ForeignKey(
        Usuarios,
        on_delete=models.SET_NULL, #EVITA QUE AL BORRAR UN USUARIO, SU FK EN LA AUDITORIA QUEDE NULL
        related_name='auditorias_usuario_usuario',
        db_column="UsuarioId",
        null=True,
        blank=True
    )

    UsuarioIdRespaldo = models.IntegerField(
        null=True,
        blank=True
    )

    UsuarioNombreRespaldo = models.CharField(
        max_length=70,
        null=True,
        blank=True
    )

    # Información de auditoría
    Accion = models.CharField(
        max_length=50,
        choices=[
            ('CREAR', 'Crear'),
            ('ACTUALIZAR', 'Actualizar'),
            ('ELIMINAR', 'Eliminar'),
            ('MOVIMIENTO', 'Movimiento de stock')
        ]
    )

    Fecha_hora = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'AuditoriaUsuario'
        constraints = [
            UniqueConstraint(fields=['IdAuditoriaUsuario'], name='unique_id_auditoria_usuario'),
        ]


    def __str__(self):
        return f"ID: {self.IdAuditoriaUsuario},  Usuario: {self.Usuario}, Nombre Usuario: {self.UsuarioNombreRespaldo}, Accion: {self.Accion}, Fecha: {self.Fecha_hora}"
#-----------------------------------------------------------------------------------------------------------------------------------#