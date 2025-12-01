# ------------------------------------------------------------------------
# Importación de módulos y clases necesarias para el modelo
# ------------------------------------------------------------------------
# models: Permite definir clases que representan tablas en la base de datos.
# UniqueConstraint: Se utiliza para establecer restricciones de unicidad a nivel de tabla.
# MinLengthValidator: Valida que un texto tenga una longitud mínima.
# ValidationError: Permite lanzar errores personalizados en validaciones.
# re: Módulo de expresiones regulares usado para comprobar formatos de texto.
# ------------------------------------------------------------------------
from django.db import models
from django.db.models import UniqueConstraint
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
import re


# ========================================================================
# Modelo: Bodegas
# ========================================================================
# Este modelo representa la tabla 'Bodegas' en la base de datos.
# Cada campo del modelo corresponde a una columna de dicha tabla.
# El uso de db_column garantiza que Django utilice los nombres exactos
# de las columnas existentes, evitando que genere nombres automáticos.
# ========================================================================
class Bodegas(models.Model):

    # --------------------------------------------------------------------
    # ID de la bodega
    # --------------------------------------------------------------------
    # AutoField: genera automáticamente un número incremental único por registro.
    # primary_key=True: define este campo como la clave primaria.
    # db_column: indica el nombre exacto de la columna en la base de datos.
    # verbose_name: define el nombre descriptivo mostrado en el panel administrativo.
    # --------------------------------------------------------------------
    IdBodega = models.AutoField(
        primary_key=True,
        db_column='IdBodega',
        verbose_name='Id Bodega'
    )
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # FUNCIÓN: validacion_no_caracteres_especiales
    # --------------------------------------------------------------------
    # Esta función valida que el texto ingresado no contenga caracteres especiales.
    # Solo se permiten:
    #   - Letras (mayúsculas y minúsculas, incluyendo acentos y Ñ)
    #   - Números
    #   - Espacios
    # Si el valor ingresado contiene símbolos o caracteres no permitidos,
    # lanza un ValidationError con un mensaje descriptivo.
    # --------------------------------------------------------------------
    def validacion_no_caracteres_especiales(value):
        expresion = r'^[A-Za-zÁÉÍÓÚáéíóúÑñ0-9 ]+$'
        if re.match(expresion, value):
            return value
        else:
            raise ValidationError('No se permiten caracteres especiales')
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # Nombre de la bodega
    # --------------------------------------------------------------------
    # CharField: almacena el nombre de la bodega (texto corto).
    # max_length: longitud máxima permitida de 20 caracteres.
    # db_column: nombre exacto de la columna en la base de datos.
    # verbose_name: etiqueta visible en el panel de administración.
    # validators:
    #   - validacion_no_caracteres_especiales: restringe caracteres no válidos.
    #   - MinLengthValidator: exige un mínimo de 5 caracteres.
    # --------------------------------------------------------------------
    NombreBodega = models.CharField(
        max_length=20,
        db_column='NombreBodega',
        verbose_name='Nombre',
        validators=[
            validacion_no_caracteres_especiales,
            MinLengthValidator(5, message="Debes ingresar minimo 5 caracteres")
        ]
    )
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # Ubicación de la bodega
    # --------------------------------------------------------------------
    # CharField: campo de texto que almacena la ubicación de la bodega.
    # max_length: longitud máxima de 30 caracteres.
    # db_column: mapea el campo a la columna exacta en la base de datos.
    # verbose_name: etiqueta visible en formularios y panel administrativo.
    # validators:
    #   - validacion_no_caracteres_especiales: prohíbe caracteres no válidos.
    #   - MinLengthValidator: exige al menos 5 caracteres.
    # --------------------------------------------------------------------
    UbicacionBodega = models.CharField(
        max_length=30,
        db_column='UbicacionBodega',
        verbose_name='Ubicacion',
        validators=[
            validacion_no_caracteres_especiales,
            MinLengthValidator(5, message="Debes ingresar minimo 5 caracteres")
        ]
    )
    # --------------------------------------------------------------------

    # Opciones disponibles para el estado de la bodega
    ESTADO_BODEGA = [
        ('Activa', 'Activa'),
        ('Inactiva', 'Inactiva'),
        ('En Mantenimiento', 'En Mantenimiento')
    ]

    # Campo para guardar el estado de la bodega
    EstadoBodega = models.CharField(
        max_length=20,                           # Máximo 20 caracteres
        choices=ESTADO_BODEGA,                   # Solo puede ser una de las opciones definidas arriba
        db_column='EstadoBodega',                # Nombre de la columna en la base de datos
        verbose_name='Estado de la bodega',      # Nombre visible en el panel de administración
    )

    # Campo para observaciones o notas adicionales
    ObservacionesBodega = models.TextField(
        max_length=500,                          # Hasta 500 caracteres permitidos
        db_column='ObservacionesBodega',         # Nombre de la columna en la base de datos
        verbose_name='Observaciones sobre la bodega',  # Nombre visible en el admin
        validators=[                             # Reglas de validación
        validacion_no_caracteres_especiales,        # No se permiten caracteres especiales
        MinLengthValidator(10, message="Debes ingresar mínimo 10 caracteres")  # Al menos 10 caracteres
        ]
    )



    # --------------------------------------------------------------------
    # Meta información del modelo
    # --------------------------------------------------------------------
    # Define configuraciones adicionales:
    #   - db_table: nombre exacto de la tabla en la base de datos.
    #   - constraints: restricciones de unicidad para evitar registros duplicados.
    # En este caso, asegura que el IdBodega sea único dentro de la tabla.
    # --------------------------------------------------------------------
    class Meta:
        db_table = 'Bodegas'
        constraints = [
            UniqueConstraint(fields=['IdBodega'], name='unique_id_bodega'),
        ]
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # MÉTODO __STR__ IMPLEMENTADO
    # --------------------------------------------------------------------
    # Devuelve una representación legible del objeto.
    # Se utiliza al mostrar registros en el panel de administración o la shell.
    # Muestra los datos más relevantes: ID, nombre y ubicación de la bodega.
    # --------------------------------------------------------------------
    def __str__(self):
        return f"NOMBRE: {self.NombreBodega}, UBICACION: {self.UbicacionBodega}"
