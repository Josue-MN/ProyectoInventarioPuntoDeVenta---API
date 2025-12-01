from django.shortcuts import render
from LoginApp.decorators import login_requerido
from CrudUsuariosApp.models import Usuarios


# Decorador personalizado que verifica si el usuario tiene una sesión activa.
# Si el usuario no está logeado, el decorador normalmente redirige al login
# antes de permitir el acceso a la vista.
@login_requerido
def renderAdminHome(request):

    # Obtiene el nombre de usuario almacenado en la sesión bajo el valor 'Usuario_Username'.
    # Esta la información que se guarda cuando el usuario inicia sesión.
    UsuarioLogeado = request.session.get('Usuario_Username')

    # Busca en la base de datos un usuario cuyo campo "Username" coincida con el valor obtenido.
    # "filter()" devuelve un queryset (lista de resultados)
    UsuarioObjeto = Usuarios.objects.filter(Username=UsuarioLogeado)

    # Crea un diccionario con los datos que se enviarán al template.
    # Aquí se pasa el queryset encontrado para que la plantilla pueda mostrar los datos del usuario.
    data = {'Usuario': UsuarioObjeto}
    
    # Renderiza la plantilla 'adminhome.html' ubicada en la carpeta templateAdminHome,
    # y le envía el diccionario "data" como contexto para usarlo dentro del HTML.
    return render(request, 'templateAdminHome/adminhome.html', data)


