from django.shortcuts import render
from LoginApp.decorators import login_requerido
from CrudUsuariosApp.models import Usuarios

# Create your views here.

# RENDER PARA EL TEMPLATE DEL HOME
@login_requerido  # Decorador que valida que el usuario esté autenticado antes de acceder a la vista
def renderTemplateHome(request):

    # Se obtiene el nombre de usuario almacenado en la sesión
    # Este valor normalmente se guarda al momento de iniciar sesión correctamente
    UsuarioLogeado = request.session.get("Usuario_Username")

    # Se consulta en la base de datos el usuario cuyo Username coincida con el nombre guardado en sesión
    # filter() devuelve un queryset, aunque solo exista un usuario.
    UsuarioObtenido = Usuarios.objects.filter(Username=UsuarioLogeado)

    # Diccionario con los datos que se enviarán al template
    data = {
        'Usuario': UsuarioObtenido  # Se envía el queryset al template para mostrar datos del usuario
    }

    # Se renderiza el template 'home.html' con los datos enviados
    return render(request, "templateHome/home.html", data)
