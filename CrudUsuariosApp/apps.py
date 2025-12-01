from django.apps import AppConfig
# Importa la señal post_migrate, la cual se ejecuta automáticamente
# después de que Django termina de aplicar las migraciones.
from django.db.models.signals import post_migrate

# Importa la función para encriptar contraseñas según el sistema de Django.
from django.contrib.auth.hashers import make_password


def crear_usuario_admin(sender, **kwargs):
    """
    Función que se ejecutará después de migrar la base de datos.
    Su propósito es crear automáticamente un usuario administrador
    si aún no existe.
    """

    # Importamos el modelo dentro de la función para evitar errores como:
    # "AppRegistryNotReady: Apps aren't loaded yet"
    from CrudUsuariosApp.models import Usuarios  

    # Verifica si NO existe un usuario con Username="Admin"
    if not Usuarios.objects.filter(Username="Admin").exists():

        # Si no existe, lo crea con credenciales predeterminadas
        Usuarios.objects.create(
            Username="Admin",
            Password=make_password("Admin123"),  # Contraseña encriptada
            CorreoElectronico="admin@gmail.com",
        )

        # Mensaje en consola para confirmar que fue creado
        print("Usuario creado automáticamente")


class CrudusuariosappConfig(AppConfig):
    """
    Configuración de la aplicación CrudUsuariosApp.
    Django ejecuta esta clase al iniciar el proyecto.
    """

    # Tipo de campo automático por defecto para claves primarias
    default_auto_field = 'django.db.models.BigAutoField'

    # Nombre de la aplicación
    name = 'CrudUsuariosApp'

    def ready(self):
        """
        El método ready() se ejecuta una vez que la aplicación está cargada.
        Aquí conectamos la señal post_migrate con la función que
        crea el usuario administrador.
        """

        # Importación interna para evitar errores de dependencias circulares
        from CrudUsuariosApp.apps import crear_usuario_admin

        # Conecta la señal post_migrate con nuestra función creadora de admin
        post_migrate.connect(crear_usuario_admin, sender=self)

