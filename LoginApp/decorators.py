from django.shortcuts import redirect
from django.views.decorators.cache import cache_control

# Este decorador evita que un usuario NO autenticado acceda a una vista.
# Verifica si existe la variable de sesión "Usuario_Username".
# Si no existe, redirige al Login.
# También incluye configuración de caché para evitar volver atrás después de cerrar sesión.
# ---------------------------------------------------------

def login_requerido(funcion_envuelta):

    # Control de cache: impide que el navegador guarde páginas protegidas,
    # evitando que el usuario navegue "hacia atrás" tras hacer logout.
    @cache_control(no_cache=True, must_revalidate=True, no_store=True)

    def funcion_reemplazada(request, *args, **kwargs):
        # Debug para ver qué usuario está en la sesión (útil en desarrollo)
        print("DEBUG -> Usuario_Username:", request.session.get("Usuario_Username"))

        # Verificación de sesión:
        # Si no existe el usuario en sesión, se redirige al login
        if not request.session.get("Usuario_Username"):
            return redirect('Login')

        # Si existe la sesión, se ejecuta la vista original
        return funcion_envuelta(request, *args, **kwargs)

    return funcion_reemplazada

# Permite acceso SOLO si el usuario logeado es "Admin".
# Caso contrario, redirige al home.
# Protege vistas administrativas sin necesidad de usar permisos de Django.
# ---------------------------------------------------------

def solo_admin(funcion_envuelta):

    # Evita que el navegador acceda a páginas cacheadas
    @cache_control(no_cache=True, must_revalidate=True, no_store=True)

    def funcion_reemplazada(request, *args, **kwargs):
        # Obtiene el usuario almacenado en la sesión
        UsuarioLogeado = request.session.get("Usuario_Username")

        # Revisa si el usuario NO es admin
        if UsuarioLogeado != "Admin":
            # Si no es admin, se redirige al home para evitar acceso
            return redirect('home')

        # Si es admin, se ejecuta la vista
        return funcion_envuelta(request, *args, **kwargs)

    return funcion_reemplazada
