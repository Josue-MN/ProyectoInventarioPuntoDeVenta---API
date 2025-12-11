# Importa la función render (aunque en esta función no se usa directamente,
# normalmente está en views porque otras vistas sí la usan para devolver templates)
from django.shortcuts import render
# Importa el modelo AuditoriaBodega, que representa la tabla donde se guardan
# los registros de auditoría (qué pasó, en qué bodega, quién lo hizo, cuándo, etc.).
from ProInvPunDeVenAPI.models import *



def RegistrarAuditoriaBodega(request, bodega, accion):
    # OBTIENE EL USUARIO QUE INICIO SESION
    user = request.user

    # INICIALIZA LA VARIABLE DE USUARIO COMO NULO
    usuario = None

    # VERIFICA QUE EL USUARIO EXISTA Y ESTE AUTENTICADO
    if user and user.is_authenticated:
        # VERIFICA SI EL USUARIO TIENE ATRIBUTO userAuthId Y NO ES NULO
        if hasattr(user, "userAuthId") and user.userAuthId:
            try:
                # OBTIENE LA INSTANCIA DE Usuarios CORRESPONDIENTE AL USER
                usuario = Usuarios.objects.get(UserAuth=user)
            except Usuarios.DoesNotExist:
                usuario = None

    # CREA EL REGISTRO DE AUDITORÍA EN LA TABLA CORRESPONDIENTE
    AuditoriaBodega.objects.create(
        Bodega=bodega,
        Usuario=usuario,
        BodegaIdRespaldo=bodega.IdBodega,
        BodegaNombreRespaldo=bodega.NombreBodega,
        Accion=accion
    )
#---------------------------------------------------------------------------#

def RegistrarAuditoriaCargo(request, cargo, accion):
    # OBTIENE EL USUARIO QUE INICIO SESION
    user = request.user
    usuario = None

    if user and user.is_authenticated:
        if hasattr(user, "userAuthId") and user.userAuthId:
            try:
                usuario = Usuarios.objects.get(UserAuth=user)
            except Usuarios.DoesNotExist:
                usuario = None

    # CREA EL REGISTRO DE AUDITORÍA PARA CARGO
    AuditoriaCargo.objects.create(
        Cargo=cargo,
        Usuario=usuario,
        CargoIdRespaldo=cargo.IdCargos,
        CargoNombreRespaldo=cargo.TipoDeCargo,
        Accion=accion
    )
#---------------------------------------------------------------------------#

def RegistrarAuditoriaCategoria(request, categoria, accion):
    # OBTIENE EL USUARIO QUE INICIO SESION
    user = request.user
    usuario = None

    if user and user.is_authenticated:
        if hasattr(user, "userAuthId") and user.userAuthId:
            try:
                usuario = Usuarios.objects.get(UserAuth=user)
            except Usuarios.DoesNotExist:
                usuario = None

    # CREA EL REGISTRO DE AUDITORÍA PARA CATEGORÍA
    AuditoriaCategoria.objects.create(
        Categoria=categoria,
        Usuario=usuario,
        CategoriaIdRespaldo=categoria.IdCategoriaProducto,
        CategoriaNombreRespaldo=categoria.NombreCategoria,
        Accion=accion
    )
#---------------------------------------------------------------------------#

def RegistrarAuditoriaEmpleado(request, empleado, accion):
    # OBTIENE EL USUARIO QUE INICIO SESION
    user = request.user
    usuario = None

    if user and user.is_authenticated:
        if hasattr(user, "userAuthId") and user.userAuthId:
            try:
                usuario = Usuarios.objects.get(UserAuth=user)
            except Usuarios.DoesNotExist:
                usuario = None

    # CREA EL REGISTRO DE AUDITORÍA PARA EMPLEADO
    AuditoriaEmpleado.objects.create(
        Empleado=empleado,
        Usuario=usuario,
        EmpleadoIdRespaldo=empleado.IdEmpleado,
        EmpleadoNombreRespaldo=empleado.NombreEmpleado,
        Accion=accion
    )
#---------------------------------------------------------------------------#

def RegistrarAuditoriaProducto(request, producto, accion):
    # OBTIENE EL USUARIO QUE INICIO SESION
    user = request.user
    usuario = None

    if user and user.is_authenticated:
        if hasattr(user, "userAuthId") and user.userAuthId:
            try:
                usuario = Usuarios.objects.get(UserAuth=user)
            except Usuarios.DoesNotExist:
                usuario = None

    # CREA EL REGISTRO DE AUDITORÍA PARA PRODUCTO
    AuditoriaProducto.objects.create(
        Producto=producto,
        Usuario=usuario,
        ProductoIdRespaldo=producto.IdProducto,
        ProductoNombreRespaldo=producto.NombreProducto,
        Accion=accion
    )
#---------------------------------------------------------------------------#

def RegistrarAuditoriaUsuario(request, usuario_obj, accion):
    # OBTIENE EL USUARIO QUE INICIO SESION
    user = request.user
    usuario_sesion = None

    if user and user.is_authenticated:
        if hasattr(user, "userAuthId") and user.userAuthId:
            try:
                usuario_sesion = Usuarios.objects.get(UserAuth=user)
            except Usuarios.DoesNotExist:
                usuario_sesion = None

    # CREA EL REGISTRO DE AUDITORÍA PARA USUARIO
    AuditoriaUsuario.objects.create(
        Usuario=usuario_sesion,
        UsuarioIdRespaldo=usuario_obj.IdUsuarios,
        UsuarioNombreRespaldo=usuario_obj.Username,
        Accion=accion
    )
#---------------------------------------------------------------------------#