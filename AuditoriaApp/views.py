# Importa la función render (aunque en esta función no se usa directamente,
# normalmente está en views porque otras vistas sí la usan para devolver templates)
from django.shortcuts import render
# Importa el modelo AuditoriaBodega, que representa la tabla donde se guardan
# los registros de auditoría (qué pasó, en qué bodega, quién lo hizo, cuándo, etc.).
from ProInvPunDeVenAPI.models import *



def RegistrarAuditoriaBodega(request, bodega, accion):
    
    # Función de utilidad para registrar una auditoría asociada a una bodega.

    # Parámetros:
    #     request → el objeto HttpRequest que trae la sesión del usuario.
    #     bodega  → instancia del modelo Bodegas (objeto ya guardado en BD).
    #     accion  → string que indica la acción realizada ("CREAR", "ACTUALIZAR", "ELIMINAR", etc.).


    usuario = None

    # request.user viene de DRF/JWT
    if request.user and request.user.is_authenticated:
        # Aquí asumes que tu modelo Usuarios tiene el mismo username que request.user
        usuario = Usuarios.objects.filter(Username=request.user.username).first()

    AuditoriaBodega.objects.create(
        Bodega=bodega,
        Usuario=usuario,
        BodegaIdRespaldo=bodega.IdBodega,
        BodegaNombreRespaldo=bodega.NombreBodega,
        Accion=accion
    )
    # Crea un nuevo registro en la tabla AuditoriaBodega.
    #
    # - Bodega=bodega
    #     Aquí se pasa el OBJETO completo de Bodegas. Django ORM automáticamente
    #     toma bodega.pk (IdBodega) y lo guarda en la columna FK 'BodegaId'.
    #
    # - Usuario=usuario
    #     Se pasa el OBJETO de Usuarios (o None). Si es un objeto válido, Django
    #     guarda usuario.pk (IdUsuarios) en la columna 'UsuarioId'.
    #     Si es None, la FK se guarda como NULL (permitido porque pusiste null=True).
    #
    # - Accion=accion
    #     Se guarda el string que indica qué se hizo (por ejemplo "REGISTRAR").
    #
    # Además, como en el modelo definiste:
    #     Fecha_hora = models.DateTimeField(auto_now_add=True)
    # Django automáticamente rellena ese campo con la fecha y hora actual
    # en el momento de crear este registro.

#---------------------------------------------------------------------------#

def RegistrarAuditoriaCargo(request, cargo, accion):
    
    username = request.session.get("Usuario_Username")
    usuario = None

    if username:
        usuario = Usuarios.objects.filter(Username=username).first()

    AuditoriaCargo.objects.create(
        Cargo=cargo,
        Usuario=usuario,
        CargoIdRespaldo=cargo.IdCargos,
        CargoNombreRespaldo=cargo.TipoDeCargo,
        Accion=accion
    )
#---------------------------------------------------------------------------#


#---------------------------------------------------------------------------#

def RegistrarAuditoriaCategoria(request, categoria, accion):
    
    username = request.session.get("Usuario_Username")
    usuario = None

    if username:
        usuario = Usuarios.objects.filter(Username=username).first()

    AuditoriaCategoria.objects.create(
        Categoria=categoria,
        Usuario=usuario,
        CategoriaIdRespaldo=categoria.IdCategoriaProducto,
        CategoriaNombreRespaldo=categoria.NombreCategoria,
        Accion=accion
    )
#---------------------------------------------------------------------------#


#---------------------------------------------------------------------------#

def RegistrarAuditoriaEmpleado(request, empleado, accion):
    
    username = request.session.get("Usuario_Username")
    usuario = None

    if username:
        usuario = Usuarios.objects.filter(Username=username).first()

    AuditoriaEmpleado.objects.create(
        Empleado=empleado,
        Usuario=usuario,
        EmpleadoIdRespaldo=empleado.IdEmpleado,
        EmpleadoNombreRespaldo=empleado.NombreEmpleado,
        Accion=accion
    )
#---------------------------------------------------------------------------#


#---------------------------------------------------------------------------#

def RegistrarAuditoriaProducto(request, producto, accion):
    
    username = request.session.get("Usuario_Username")
    usuario = None

    if username:
        usuario = Usuarios.objects.filter(Username=username).first()

    AuditoriaProducto.objects.create(
        Producto=producto,
        Usuario=usuario,
        ProductoIdRespaldo=producto.IdProducto,
        ProductoNombreRespaldo=producto.NombreProducto,
        Accion=accion
    )
#---------------------------------------------------------------------------#


#---------------------------------------------------------------------------#

def RegistrarAuditoriaUsuario(request, usuario, accion):

    username = request.session.get("Usuario_Username")
    usuarioSesion = None

    if username:
        usuarioSesion = Usuarios.objects.filter(Username=username).first()

    AuditoriaUsuario.objects.create(
        Usuario=usuarioSesion,
        UsuarioIdRespaldo=usuario.IdUsuarios,
        UsuarioNombreRespaldo=usuario.Username,
        Accion=accion
    )
#---------------------------------------------------------------------------#