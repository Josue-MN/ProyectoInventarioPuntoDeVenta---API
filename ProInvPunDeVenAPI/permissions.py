#A TRAVES DE REST_FRAMEWORK Y PERMISOS SE IMPORTA LA CLASE DE BASEPERMISSION QUE PUEDE DAR
#O OBTENER PERMISOS DE TODOO O UN OBJECTO EN ESPECIFICO 
from rest_framework.permissions import BasePermission

#CLASE DE PERMISO QUE VALIDA QUE EL USUARIO TENGA EL ROL ADMINISTRADOR PARA DAR A CONOCEER
#LO QUE PUEDE HACER EN LA PAGINA
class EsUsuarioAdmin(BasePermission):
    def has_permission(self, request, view):
        #OBTIENE EL USUARIO QUE INICIO SESION
        user = request.user

        #SE ASEGURA QUE EL USUARIO EXISTA Y QUE ESTE AUTHENTICADO PARA CONTINUAR
        if not user or not user.is_authenticated:
            return False
        
        ##OBTIENE EL CARGO DEL USUARIO OBTENIDO
        cargo = getattr(user.cargo, 'TipoDeCargo', '')

        ##DEVUELVE EL CARGO CON EL ROL ADMINISTRADOR
        return cargo == 'Administrador'

#CLASE DE PERMISO QUE VALIDA QUE EL USUARIO TENGA EL ROL EMPLEADO PARA DAR A CONOCEER
#LO QUE PUEDE HACER EN LA PAGINA
class EsUsuarioBasico(BasePermission):
    def has_permission(self, request, view):
        #OBTIENE EL USUARIO QUE INICIO SESION
        user = request.user

        #SE ASEGURA QUE EL USUARIO EXISTA Y QUE ESTE AUTHENTICADO PARA CONTINUAR
        if not user or not user.is_authenticated:
            return False
        
        ##OBTIENE EL CARGO DEL USUARIO OBTENIDO
        cargo = getattr(user.cargo, 'TipoDeCargo', '')

        ##SI EL CARGO OBTENIDO ES EMPLEADO LE PERMITE AL USUARIO VER COSAS EN LA PAGINA
        if cargo == "Empleado":
            ##SEGUN EL METODO QUE PUEDE HACER
            return request.method in ['GET', 'HEAD', 'OPTIONS']

        #PARA FINALMENTE DEVOLVER EL CARGO ADMINISTRADOR EN CASO DE QUE NO SEA EMPLEADO
        return cargo == 'Administrador'