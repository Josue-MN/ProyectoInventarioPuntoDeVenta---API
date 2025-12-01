# ------------------------------------------------------------------------
# Importación de módulos y clases necesarias para el modelo
# ------------------------------------------------------------------------
# models: Permite definir clases que representan tablas de la base de datos.
# UniqueConstraint: Define restricciones de unicidad a nivel de tabla.
# MinLengthValidator: Valida que el texto tenga una longitud mínima.
# ValidationError: Se utiliza para lanzar errores personalizados en validaciones.
# re: Módulo de expresiones regulares, usado para verificar formatos de texto.
# ------------------------------------------------------------------------
from django.db import models
from django.db.models import UniqueConstraint
from django.core.validators import MinLengthValidator, EmailValidator
from django.core.exceptions import ValidationError
import re
from CrudEmpleadosApp.models import Empleados ##Para usar con llaves foraneas
from CrudCargosApp.models import Cargos ##Para usar con llaves foraneas

# ========================================================================
# Modelo: Usuarios
# ========================================================================
# Este modelo representa la tabla 'Usuarios' en la base de datos.
# Se utiliza db_column para mapear cada campo del modelo a su columna
# existente, evitando que Django cree nuevas columnas con nombres automáticos.
# ========================================================================
class Usuarios(models.Model):

    # --------------------------------------------------------------------
    # ID del usuario
    # --------------------------------------------------------------------
    # AutoField: campo autoincremental que genera un identificador único.
    # primary_key=True: define este campo como clave primaria.
    # db_column: nombre exacto de la columna en la base de datos.
    # --------------------------------------------------------------------
    IdUsuarios = models.AutoField(
        primary_key=True, 
        db_column='IdUsuarios'
    )
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # Nombre de usuario (Username)
    # --------------------------------------------------------------------
    # CharField: campo de texto que almacena el nombre de usuario.
    # max_length: longitud máxima de 30 caracteres.
    # validators: valida que el nombre tenga al menos 5 caracteres.
    # db_column: nombre exacto de la columna en la base de datos.
    # error_messages: mensaje personalizado si el nombre ya existe (único).
    # --------------------------------------------------------------------
    Username = models.CharField(
        max_length=30, 
        db_column='Username',
        validators=[MinLengthValidator(5, message="El username debe tener al menos 5 caracteres")],
        error_messages={'unique': 'El username ingresado ya se encuentra ocupado, Por favor, intentelo con otro nuevamente.'}
    )
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # FUNCIÓN: validacion_password_segura
    # --------------------------------------------------------------------
    # Esta función valida que la contraseña cumpla con los requisitos mínimos
    # de seguridad:
    #  - Contenga al menos una letra (mayúscula o minúscula)
    #  - Contenga al menos un número
    # Se utiliza una expresión regular (regex) para verificarlo.
    # Si la validación falla, lanza un ValidationError con un mensaje descriptivo.
    # --------------------------------------------------------------------
    def validacion_password_segura(value):
        expresion = r'^(?=.*[a-zA-Z])(?=.*[0-9]).*$'
        if re.search(expresion, value):
            return value
        else:
            raise ValidationError('La password ingresada debe contener al menos 1 letra y 1 numero')
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # Contraseña del usuario
    # --------------------------------------------------------------------
    # CharField: almacena el texto de la contraseña (en texto plano o encriptado).
    # max_length: longitud máxima de 45 caracteres.
    # validators:
    #   - validacion_password_segura: asegura complejidad mínima.
    #   - MinLengthValidator: obliga a tener al menos 5 caracteres.
    # db_column: mapea al campo real en la base de datos.
    # --------------------------------------------------------------------
    Password = models.CharField(
        max_length=128, 
        db_column='Password',
        validators=[
            validacion_password_segura,
            MinLengthValidator(5, message="La password debe tener al menos 5 caracteres")
        ]
    )
    # --------------------------------------------------------------------



    # ============================================================
    # Campo de correo electrónico
    # ============================================================
    CorreoElectronico = models.EmailField(
        max_length=100,  # Longitud máxima permitida
        db_column='CorreoElectronico',  # Nombre de columna en la base de datos
        verbose_name='Correo electronico',  # Etiqueta legible en el admin y formularios
        validators=[EmailValidator(message="Debe ingresar un correo valido")],  # Valida formato de correo
        error_messages={
            'unique': 'El correo electronico ingresado ya se encuentra ocupado, Por favor, intentelo con otro nuevamente.'
        }  # Mensaje personalizado si el correo ya existe
    )

    ###LLAVES FORANEAS###
    Empleado = models.ForeignKey(
        Empleados, #Modelo Relacionado
        on_delete=models.SET_NULL,
        related_name="usuario", #Para acceder a el desde categoria
        db_column="EmpleadoId", #Nombre que tendra en la base de datos
        null=True, #Si puede quedar nulo
        blank=True #Si puede quedar vacio
        #SI NULL Y BLANK QUEDAN EN FALSE LA VALIDACION PERSONALIZADA QUEDA INACTIVA
    )

    Cargo = models.ForeignKey(
        Cargos, #Modelo Relacionado
        on_delete=models.SET_NULL,
        related_name="cargo", #Para acceder a el desde categoria
        db_column="CargoId", #Nombre que tendra en la base de datos
        null=True, #Si puede quedar nulo
        blank=True #Si puede quedar vacio
        #SI NULL Y BLANK QUEDAN EN FALSE LA VALIDACION PERSONALIZADA QUEDA INACTIVA
    )
    
    # --------------------------------------------------------------------
    # Meta información del modelo
    # --------------------------------------------------------------------
    # Clase interna que define configuraciones adicionales del modelo:
    #  - db_table: nombre exacto de la tabla en la base de datos.
    #  - constraints: restricciones de unicidad para campos específicos.
    #    Evita que se repitan IDs o usernames dentro de la tabla.
    # --------------------------------------------------------------------
    class Meta:
        db_table = 'Usuarios'
        constraints = [
            UniqueConstraint(fields=['IdUsuarios'], name='unique_id_usuarios'),
            UniqueConstraint(fields=['Username'], name='unique_username'),
            UniqueConstraint(fields=['CorreoElectronico'], name='unique_correo_electronico'),
        ]
    # --------------------------------------------------------------------

    

    #models.CASCADE → borra también el relacionado.
    #models.PROTECT → impide borrarlo si está en uso.
    #models.SET_NULL → pone NULL en la FK.
    #models.SET_DEFAULT → asigna valor por defecto

    #default="Sin valor", #Lo que ocurrre segun la lista de abajo si se elimina

    # --------------------------------------------------------------------
    # MÉTODO __STR__ IMPLEMENTADO
    # --------------------------------------------------------------------
    # Devuelve una representación legible del objeto.
    # Es útil al mostrar registros en el panel de administración de Django
    # o en la consola interactiva. Muestra los datos más importantes del usuario.
    # --------------------------------------------------------------------
    def __str__(self):
        return f"ID: {self.IdUsuarios}, USERNAME: {self.Username}, CORREO ELECTRONICO: {self.CorreoElectronico}"
