# ------------------------------------------------------------------------
# Importación de módulos y clases necesarias para el modelo
# ------------------------------------------------------------------------
# models: Permite definir clases que representan tablas de la base de datos.
# UniqueConstraint: Permite establecer restricciones de unicidad entre campos.
# Validadores y excepciones: Se usan para controlar reglas de negocio y errores.
# re: Módulo para trabajar con expresiones regulares (validación de texto).
# ------------------------------------------------------------------------
from django.db import models
from django.db.models import UniqueConstraint
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
import re


# ------------------------------------------------------------------------
# Modelo: Empleados
# ------------------------------------------------------------------------
# Este modelo representa la tabla 'Empleados' en la base de datos.
# Cada atributo de la clase se convierte en una columna de la tabla.
# Se usa db_column para asegurar que el nombre coincida exactamente con el
# de la base de datos existente (evita que Django genere uno automático).
# ------------------------------------------------------------------------
class Empleados(models.Model):
    
    # --------------------------------------------------------------------
    # ID del empleado
    # --------------------------------------------------------------------
    # AutoField: Genera automáticamente un número incremental para cada registro.
    # primary_key=True: Define que este campo será la clave primaria.
    # db_column: Nombre exacto de la columna en la base de datos.
    # --------------------------------------------------------------------
    IdEmpleado = models.AutoField(
        primary_key=True, 
        db_column='IdEmpleado'
    )
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # FUNCIÓN: validacion_rut_real
    # --------------------------------------------------------------------
    # Esta función valida que el RUT tenga el formato correcto:
    # 7 u 8 números seguidos de un guion y un dígito o la letra 'K'.
    # Ejemplo válido: 12345678-9 o 1234567-K
    # Si no cumple, se lanza un ValidationError que Django mostrará en el admin.
    # --------------------------------------------------------------------
    def validacion_rut_real(value):
        expresion = r"^\d{7,8}-[\dK]$"
        if re.match(expresion, value):
            return value
        else:
            raise ValidationError('Ingrese un rut valido (01234567-k) con guion y sin puntos.')
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # RUT del empleado
    # --------------------------------------------------------------------
    # CharField: campo de texto para almacenar el RUT.
    # max_length: limita la cantidad máxima de caracteres.
    # verbose_name: etiqueta legible que se mostrará en el panel de administración.
    # validators: lista de funciones que validan el valor ingresado.
    # error_messages: personaliza el mensaje que aparece si se viola una restricción.
    # --------------------------------------------------------------------
    RutEmpleado = models.CharField(
        max_length=10, 
        db_column='RutEmpleado', 
        verbose_name="Rut (01234567-k)",
        validators=[validacion_rut_real],
        error_messages={'unique': 'El rut ingresado ya se encuentra registrado, Por favor, verifique.'}
    )
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # FUNCIÓN: validacion_nombre_y_apellido_real
    # --------------------------------------------------------------------
    # Esta validación se aplica a nombre y apellido.
    # Asegura que el valor contenga solo letras (incluyendo acentos) y espacios.
    # No permite números ni caracteres especiales.
    # --------------------------------------------------------------------
    def validacion_nombre_y_apellido_real(value):
        expresion = r"^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+$"
        if re.match(expresion, value):
            return value
        else:
            raise ValidationError('No se permiten numeros y caracteres especiales')
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # Nombre del empleado
    # --------------------------------------------------------------------
    # CharField: texto corto, limitado a 20 caracteres.
    # Se valida que tenga un mínimo de 3 letras y solo contenga caracteres válidos.
    # --------------------------------------------------------------------
    NombreEmpleado = models.CharField(
        max_length=20, 
        db_column='NombreEmpleado', 
        verbose_name="Nombre",
        validators=[
            validacion_nombre_y_apellido_real,    
            MinLengthValidator(3, message="Por favor, ingrese un nombre real")
        ]
    )
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # Apellido del empleado
    # --------------------------------------------------------------------
    # Similar al nombre, pero permite hasta 55 caracteres.
    # Se usa el mismo validador de letras y el mismo mínimo de longitud.
    # --------------------------------------------------------------------
    ApellidoEmpleado = models.CharField(
        max_length=55, 
        db_column='ApellidoEmpleado', 
        verbose_name="Apellido",
        validators=[
            validacion_nombre_y_apellido_real,    
            MinLengthValidator(3, message="Por favor, ingrese un apellido real")
        ]
    )
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # FUNCIÓN: validacion_edad_negativa
    # --------------------------------------------------------------------
    # Esta función evita que se ingresen edades negativas.
    # Si el valor es menor que 0, lanza un ValidationError.
    # --------------------------------------------------------------------
    def validacion_edad_negativa(value):
        if value < 0:
            raise ValidationError('No se permiten edades negativas')
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # Edad del empleado
    # --------------------------------------------------------------------
    # IntegerField: almacena valores numéricos enteros.
    # Se aplican validaciones para asegurar que:
    #  - No sea negativa.
    #  - Sea mayor o igual a 18 años.
    #  - Sea menor o igual a 99 años.
    # --------------------------------------------------------------------
    EdadEmpleado = models.IntegerField(
        db_column='EdadEmpleado', 
        verbose_name="Edad",
        validators=[
            validacion_edad_negativa,
            MinValueValidator(18, message="Debes tener al menos 18 años"),
            MaxValueValidator(99, message="Edad invalida, no puede tener mas de 100 años")
        ]
    )
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # FUNCIÓN: validacion_largo_y_solo_numeros
    # --------------------------------------------------------------------
    # Esta función valida que el número telefónico:
    #  - No sea negativo.
    #  - Contenga exactamente 9 dígitos.
    #  - Empiece con el número 9 (formato chileno).
    #  - Contenga solo números (sin espacios ni letras).
    # Si alguna condición falla, se lanza un ValidationError con el motivo.
    # --------------------------------------------------------------------
    def validacion_largo_y_solo_numeros(value):
        expresion = r"^9\d{8}$"
        validarInput = str(value)
        if value < 0:
            raise ValidationError('No se permiten numeros negativos')
        if len(validarInput) != 9:
            raise ValidationError('El numero telefonico debe tener exactamente 9 digitos')
        if not validarInput.isdigit():
            raise ValidationError('Solo se permiten números')
        if re.match(expresion, validarInput):
            return value
        else:
            raise ValidationError("El número debe comenzar con 9 y tener exactamente 9 dígitos numéricos.")
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # Teléfono del empleado
    # --------------------------------------------------------------------
    # IntegerField: almacena el número telefónico sin formato (solo dígitos).
    # verbose_name: etiqueta visible para el administrador de Django.
    # validators: aplica la función anterior para validar el formato.
    # --------------------------------------------------------------------
    NumeroTelefonoEmpleado = models.IntegerField(
        db_column='NumeroTelefonoEmpleado', 
        verbose_name="Telefono (912345678)",
        validators=[validacion_largo_y_solo_numeros]
    )
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # Meta información del modelo
    # --------------------------------------------------------------------
    # Esta clase interna configura detalles adicionales del modelo:
    #  - db_table: especifica el nombre real de la tabla en la base de datos.
    #  - constraints: define restricciones de unicidad (no se repiten valores).
    # --------------------------------------------------------------------
    class Meta:
        db_table = 'Empleados'
        constraints = [
            # Asegura que no haya dos registros con el mismo ID.
            UniqueConstraint(fields=['IdEmpleado'], name='unique_id_empleado'),
            # Asegura que el RUT sea único entre todos los empleados.
            UniqueConstraint(fields=['RutEmpleado'], name='unique_rut_empleado'),
        ]
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # MÉTODO __STR__ IMPLEMENTADO
    # --------------------------------------------------------------------
    # Este método devuelve una representación legible del objeto.
    # Se usa cuando el objeto se muestra en el panel de administración o en la shell.
    # Muestra los datos principales del empleado en una sola línea.
    # --------------------------------------------------------------------
    def __str__(self):
        return f"Nombre Completo: {self.NombreEmpleado} {self.ApellidoEmpleado}, Rut: {self.RutEmpleado}"
