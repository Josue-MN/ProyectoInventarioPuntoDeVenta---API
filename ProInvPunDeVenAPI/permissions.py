"""
Permisos personalizados por rol. Cada clase valida el Cargo asociado al
usuario autenticado (via UserAuth) y determina que metodos HTTP puede usar.
Admin siempre pasa; otros roles se limitan a GET o CRUD segun configuracion.
"""

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

        #CREA LA VARIABLE VACIA COMO SEÑUELO PARA QUE NO DE ERROR DE NO TENER CARGO
        cargo = None 

        ##PRIMERO VERIFICA QUE SI USER TIENE UN ATRIBUTO LLAMADO userAuthId Y CON HASATTR SE EVITA 
        ##SI HAY UN ERROR QUE TOODO COLAPSE

        ##Y USER.USERAUTHID VERIFICA QUE EL CARGO NO SEA NULO EN LA BASE DE DATOS
        if hasattr(user, "userAuthId") and user.userAuthId and user.userAuthId.Cargo:
            cargo = user.userAuthId.Cargo.TipoDeCargo

        ##OBTIENE EL USERNAME
        usernameAuth = user.username.lower()

        ##DEVUELVE EL CARGO CON EL ROL ADMINISTRADOR
        return (cargo == 'Administrador') or (usernameAuth == "admin")

#CLASE DE PERMISO QUE VALIDA QUE EL USUARIO TENGA EL ROL EMPLEADO PARA DAR A CONOCEER
#LO QUE PUEDE HACER EN LA PAGINA
class EsUsuarioBasicos(BasePermission):


    CARGOS_DEL_USUARIO = ["Etiquetador", "Ayudante", "Despachador"]

    def has_permission(self, request, view):
        #OBTIENE EL USUARIO QUE INICIO SESION
        user = request.user

        #SE ASEGURA QUE EL USUARIO EXISTA Y QUE ESTE AUTHENTICADO PARA CONTINUAR
        if not user or not user.is_authenticated:
            return False
        
        ##OBTIENE EL CARGO DEL USUARIO OBTENIDO

        #CREA LA VARIABLE VACIA COMO SEÑUELO PARA QUE NO DE ERROR DE NO TENER CARGO
        cargo = None 

        ##Y USER.USERAUTHID VERIFICA QUE EL CARGO NO SEA NULO EN LA BASE DE DATOS
        if hasattr(user, "userAuthId") and user.userAuthId and user.userAuthId.Cargo:
            cargo = user.userAuthId.Cargo.TipoDeCargo
            ##SI EL CARGO OBTENIDO ES UNO DE LOS SIGUIENTES LE PERMITE AL USUARIO VER COSAS EN LA PAGINA
            if cargo in self.CARGOS_DEL_USUARIO:
                ##SEGUN EL METODO QUE PUEDE HACER
                return request.method in ['GET']

        ##OBTIENE EL USERNAME
        usernameAuth = user.username.lower()

        #PARA FINALMENTE DEVOLVER EL CARGO ADMINISTRADOR EN CASO DE QUE NO SEA USUARIO BASICO
        return (cargo == 'Administrador') or (usernameAuth == "admin")
    

#CLASE DE PERMISO QUE VALIDA QUE EL USUARIO TENGA EL ROL BODEGUERO PARA DAR A CONOCEER
#LO QUE PUEDE HACER EN LA PAGINA
class EsUsuarioBodeguero(BasePermission):


    CARGOS_DEL_USUARIO = ["Bodeguero"]

    def has_permission(self, request, view):
        #OBTIENE EL USUARIO QUE INICIO SESION
        user = request.user

        #SE ASEGURA QUE EL USUARIO EXISTA Y QUE ESTE AUTHENTICADO PARA CONTINUAR
        if not user or not user.is_authenticated:
            return False
        
        ##OBTIENE EL CARGO DEL USUARIO OBTENIDO

        #CREA LA VARIABLE VACIA COMO SEÑUELO PARA QUE NO DE ERROR DE NO TENER CARGO
        cargo = None 

        ##Y USER.USERAUTHID VERIFICA QUE EL CARGO NO SEA NULO EN LA BASE DE DATOS
        if hasattr(user, "userAuthId") and user.userAuthId and user.userAuthId.Cargo:
            cargo = user.userAuthId.Cargo.TipoDeCargo
            ##SI EL CARGO OBTENIDO ES UNO DE LOS SIGUIENTES LE PERMITE AL USUARIO VER COSAS EN LA PAGINA
            if cargo in self.CARGOS_DEL_USUARIO:
                ##SEGUN EL METODO QUE PUEDE HACER
                return request.method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'] and cargo == "Bodeguero"

        ##OBTIENE EL USERNAME
        usernameAuth = user.username.lower()

        #PARA FINALMENTE DEVOLVER EL CARGO ADMINISTRADOR EN CASO DE QUE NO SEA USUARIO BASICO
        return (cargo == 'Administrador') or (usernameAuth == "admin")
    