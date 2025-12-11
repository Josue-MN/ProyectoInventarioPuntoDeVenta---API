from django.db import models
from django.db.models import UniqueConstraint
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator, EmailValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
import re
from django.contrib.auth.models import User

# Create your models here.
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




# ========================================================================
# Modelo: Cargos
# ========================================================================
# Este modelo representa la tabla 'Cargos' en la base de datos.
# Cada atributo de la clase se mapea directamente a una columna de dicha tabla.
# El uso de db_column asegura que los nombres de las columnas coincidan exactamente
# con los de la base de datos, evitando que Django cree nombres por defecto.
# ========================================================================
class Cargos(models.Model):

    
    # --------------------------------------------------------------------
    # ID del cargo
    # --------------------------------------------------------------------
    # AutoField: crea un campo autoincremental único por cada registro.
    # primary_key=True: lo define como la clave primaria de la tabla.
    # db_column: indica el nombre exacto del campo en la base de datos.
    # verbose_name: etiqueta legible que se muestra en el panel de administración.
    # --------------------------------------------------------------------
    IdCargos = models.AutoField(
        primary_key=True,
        db_column='IdCargos',
        verbose_name='Id Cargo'
    )
    # --------------------------------------------------------------------

    # --------------------------------------------------------------------
    # OPCIONES DISPONIBLES: Tipo de Cargo
    # --------------------------------------------------------------------
    # Se define una lista de tuplas con las opciones posibles para el campo TipoDeCargo.
    # Este patrón se usa con el parámetro 'choices' para restringir los valores válidos.
    # Ejemplo:
    #   - 'Gerente'
    #   - 'Bodeguero'
    # --------------------------------------------------------------------
    TIPO_DE_CARGO = [
        ('Administrador', 'Administrador'),
        ('Etiquetador', 'Etiquetador'),
        ('Bodeguero', 'Bodeguero'),
        ('Ayudante', 'Ayudante'),
        ('Despachador', 'Despachador'),
    ]
    # --------------------------------------------------------------------

    # --------------------------------------------------------------------
    # Tipo de cargo
    # --------------------------------------------------------------------
    # CharField: almacena el tipo de cargo en formato de texto.
    # max_length: limita el número máximo de caracteres (10).
    # choices: define un conjunto cerrado de valores válidos (TIPO_DE_CARGO).
    # db_column: nombre de la columna en la base de datos.
    # verbose_name: nombre descriptivo mostrado en la interfaz del admin.
    # --------------------------------------------------------------------
    TipoDeCargo = models.CharField(
        max_length=20,
        choices=TIPO_DE_CARGO,
        db_column='TipoDeCargo',
        verbose_name='Tipo de cargo'
    )
    # --------------------------------------------------------------------

    ESTADOS = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]

    # --------------------------------------------------------------------
    # Estado del cargo
    # --------------------------------------------------------------------
    # CharField: almacena el estado actual del cargo (por ejemplo: "Activo", "Inactivo").
    # max_length: longitud máxima de 20 caracteres.
    # db_column: nombre real de la columna en la base de datos.
    # verbose_name: etiqueta visible en formularios y el panel administrativo.
    # validators:
    #   - MinLengthValidator: asegura que el texto tenga al menos 4 caracteres.
    # --------------------------------------------------------------------
    EstadoDelCargo = models.CharField(
        max_length=10,
        choices=ESTADOS,
        db_column='EstadoDelCargo',
        verbose_name='Estado del cargo'
    )
    # --------------------------------------------------------------------


    # Campo para almacenar la descripción del cargo
    DescripcionDelCargo = models.TextField(
        max_length=500,  # Máximo de 500 caracteres
        db_column='DescripcionDelCargo',  # Nombre de la columna en la base de datos
        verbose_name='Descripcion del cargo',  # Nombre legible en el admin
        validators=[MinLengthValidator(10, message='Debe ingresar al menos 10 caracteres')]  # Valida que tenga al menos 10 caracteres
    )

    # Campo para almacenar el sueldo base del cargo
    SueldoBase = models.IntegerField(
        db_column='SueldoBase',  # Nombre de la columna en la base de datos
        verbose_name='Sueldo base',  # Nombre legible en el admin
        validators=[MinValueValidator(150000, message='Sueldo base minimo es de $150.000')]  # Valida que sea mínimo $150.000
    )

    # --------------------------------------------------------------------
    # Meta información del modelo
    # --------------------------------------------------------------------
    # Define configuraciones adicionales de la clase:
    #   - db_table: nombre exacto de la tabla que Django debe usar.
    #   - constraints: define restricciones de unicidad a nivel de tabla.
    # En este caso, asegura que el IdCargos no se repita en la tabla.
    # --------------------------------------------------------------------
    class Meta:
        db_table = 'Cargos'
        constraints = [
            UniqueConstraint(fields=['IdCargos'], name='unique_id_cargos'),
        ]
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # MÉTODO __STR__ IMPLEMENTADO
    # --------------------------------------------------------------------
    # Este método devuelve una representación legible del objeto.
    # Es útil para mostrar la información en el panel de administración
    # y para depuración, mostrando los datos principales del cargo.
    # --------------------------------------------------------------------
    def __str__(self):
        return f"Tipo de Cargo: {self.TipoDeCargo}, Descripcion del cargo: {self.DescripcionDelCargo}, Sueldo base: {self.SueldoBase}"



# ========================================================================
# Modelo: CategoriaProducto
# ========================================================================
# Este modelo representa la tabla 'CategoriaProducto' en la base de datos.
# Cada campo del modelo se mapea directamente a una columna de dicha tabla.
# El parámetro db_column asegura que Django utilice los nombres exactos
# de las columnas existentes, evitando la creación de nuevas columnas por defecto.
# ========================================================================
class CategoriaProducto(models.Model):

    # --------------------------------------------------------------------
    # ID de la categoría de producto
    # --------------------------------------------------------------------
    # AutoField: genera automáticamente un valor incremental por cada registro.
    # primary_key=True: define este campo como la clave primaria.
    # db_column: asigna el nombre exacto de la columna en la base de datos.
    # verbose_name: define el nombre descriptivo que se mostrará en el panel admin.
    # --------------------------------------------------------------------
    IdCategoriaProducto = models.AutoField(
        primary_key=True,
        db_column='IdCategoriaProducto',
        verbose_name='Id Categoria Producto'
    )
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # FUNCIÓN: validacion_no_caracteres_especiales
    # --------------------------------------------------------------------
    # Esta función valida que el texto ingresado no contenga caracteres especiales.
    # Permite únicamente:
    #   - Letras (mayúsculas y minúsculas, incluyendo acentos y Ñ)
    #   - Números
    #   - Espacios
    # Si se ingresan caracteres no permitidos, lanza un ValidationError.
    # --------------------------------------------------------------------
    def validacion_no_caracteres_especiales(value):
        expresion = r'^[A-Za-zÁÉÍÓÚáéíóúÑñ0-9 ]+$'
        if re.match(expresion, value):
            return value
        else:
            raise ValidationError('No se permiten caracteres especiales')
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # Nombre de la categoría
    # --------------------------------------------------------------------
    # CharField: campo de texto corto que almacena el nombre de la categoría.
    # max_length: longitud máxima de 20 caracteres.
    # db_column: nombre real de la columna en la base de datos.
    # verbose_name: etiqueta visible en formularios y panel administrativo.
    # validators:
    #   - validacion_no_caracteres_especiales: prohíbe símbolos o caracteres no válidos.
    #   - MinLengthValidator: obliga a ingresar al menos 5 caracteres.
    # --------------------------------------------------------------------
    NombreCategoria = models.CharField(
        max_length=20,
        db_column='NombreCategoria',
        verbose_name='Nombre de la categoria',
        validators=[
            validacion_no_caracteres_especiales,
            MinLengthValidator(3, message="Debes ingresar minimo 3 caracteres")
        ]
    )
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # Descripción de la categoría
    # --------------------------------------------------------------------
    # TextField: campo de texto largo, ideal para descripciones detalladas.
    # max_length: establece un límite máximo de 500 caracteres.
    # db_column: indica el nombre exacto de la columna en la base de datos.
    # verbose_name: nombre descriptivo mostrado en formularios.
    # validators:
    #   - validacion_no_caracteres_especiales: prohíbe símbolos o caracteres no válidos.
    #   - MinLengthValidator: obliga a ingresar al menos 10 caracteres.
    # --------------------------------------------------------------------
    Descripcion = models.TextField(
        max_length=500,
        db_column='Descripcion',
        verbose_name='Descripcion',
        validators=[
            validacion_no_caracteres_especiales,
            MinLengthValidator(10, message="Debes ingresar minimo 10 caracteres")
        ]
    )
    # --------------------------------------------------------------------
    # Lista de opciones posibles para el estado de la categoría
    ESTADO = [
        ('Activo', 'Activo'),      # La categoría está activa
        ('Pausado', 'Pausado'),    # La categoría está pausada
    ]

    # --------------------------------------------------------------------
    # Campo Estado del modelo
    Estado = models.CharField(
        max_length=10,    # Máxima longitud de 10 caracteres
        choices=ESTADO,   # Se limita a las opciones definidas en ESTADO
        db_column='Estado',  # Nombre de la columna en la base de datos
    )
    # --------------------------------------------------------------------

    # Campo Observaciones del modelo
    Observaciones = models.TextField(
        max_length=500,          # Máxima longitud de 500 caracteres
        db_column='Observaciones',  # Nombre de la columna en la base de datos
        verbose_name='Observaciones',  # Etiqueta legible para formularios y admin
        validators=[             # Validadores personalizados
            validacion_no_caracteres_especiales,  # No permite caracteres especiales
            MinLengthValidator(10, message="Debes ingresar minimo 10 caracteres")  # Requiere al menos 10 caracteres
        ]
    )

    # --------------------------------------------------------------------
    # Meta información del modelo
    # --------------------------------------------------------------------
    # Define configuraciones adicionales del modelo:
    #   - db_table: nombre exacto de la tabla en la base de datos.
    #   - constraints: restricciones de unicidad para evitar duplicados.
    # En este caso, garantiza que no existan dos categorías con el mismo ID.
    # --------------------------------------------------------------------
    class Meta:
        db_table = 'CategoriaProducto'
        constraints = [
            UniqueConstraint(fields=['IdCategoriaProducto'], name='unique_id_categoria_producto'),
        ]
        
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # MÉTODO __STR__ IMPLEMENTADO
    # --------------------------------------------------------------------
    # Devuelve una representación legible del objeto.
    # Es útil para mostrar registros de forma clara en el panel de administración
    # o en la shell de Django. Muestra los campos principales de la categoría.
    # --------------------------------------------------------------------
    def __str__(self):
        return f"NOMBRE: {self.NombreCategoria}, DESCRIPCION: {self.Descripcion}"




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



# ========================================================================
# Modelo: Productos
# ========================================================================
# Representa la tabla 'Productos' en la base de datos.
# Cada atributo de la clase corresponde a una columna de la tabla.
# Se usa db_column para mapear cada campo a una columna específica
# existente en la base de datos, evitando que Django genere nombres automáticos.
# ========================================================================
class Productos(models.Model):

    # --------------------------------------------------------------------
    # ID del producto
    # --------------------------------------------------------------------
    # AutoField: campo autoincremental que genera automáticamente un valor único.
    # primary_key=True: define el campo como clave primaria de la tabla.
    # db_column: nombre exacto de la columna en la base de datos.
    # --------------------------------------------------------------------
    IdProducto = models.AutoField(
        primary_key=True,
        db_column='IdProducto'
    )
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # Código de barras del producto
    # --------------------------------------------------------------------
    # CharField: campo de texto de longitud variable.
    # max_length: define el número máximo de caracteres permitidos (100).
    # db_column: nombre de la columna en la base de datos.
    # verbose_name: texto descriptivo mostrado en formularios o panel de admin.
    # error_messages: mensaje personalizado en caso de violar una restricción.
    # --------------------------------------------------------------------
    CodigoDeBarras = models.CharField(
        max_length=100,
        db_column='CodigoDeBarras',
        verbose_name="Código de Barras",
        error_messages={'unique': 'El código de barras ingresado ya se encuentra registrado. Por favor, verifique.'}
    )
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # Valor del producto
    # --------------------------------------------------------------------
    # IntegerField: campo numérico entero que almacena el valor monetario.
    # validators: asegura que el valor mínimo permitido sea $1000.
    # verbose_name: texto legible que se muestra en el panel de administración.
    # --------------------------------------------------------------------
    ValorProducto = models.IntegerField(
        db_column='ValorProducto',
        verbose_name="Valor",
        validators=[MinValueValidator(1000, message="El valor minimo de un producto es de $1000")]
    )
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # Stock del producto
    # --------------------------------------------------------------------
    # IntegerField: campo numérico entero que almacena la cantidad disponible.
    # validators: establece que debe haber al menos 1 unidad en stock.
    # verbose_name: nombre descriptivo mostrado en la interfaz administrativa.
    # --------------------------------------------------------------------
    StockProducto = models.IntegerField(
        db_column='StockProducto',
        verbose_name="Stock",
        validators=[MinValueValidator(1, message="El Stock minimo es de 1 unidad ")]
    )
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # Nombre del producto
    # --------------------------------------------------------------------
    # CharField: campo de texto para el nombre.
    # max_length: establece un máximo de 60 caracteres.
    # validators: obliga a que el nombre tenga al menos 5 caracteres.
    # --------------------------------------------------------------------
    NombreProducto = models.CharField(
        max_length=60,
        db_column='NombreProducto',
        verbose_name="Nombre del producto",
        validators=[MinLengthValidator(5, message="El nombre del producto debe tener al menos 5 caracteres.")]
    )
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # Fecha de registro del producto
    # --------------------------------------------------------------------
    # DateTimeField: almacena fecha y hora.
    # auto_now_add=True: Django asigna automáticamente la fecha y hora actuales
    # cuando el producto se crea por primera vez.
    # db_column: nombre de la columna en la base de datos.
    # --------------------------------------------------------------------
    FechaDeRegistroProducto = models.DateTimeField(
        auto_now_add=True,
        db_column='FechaDeRegistroProducto'
    )
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # Marca del producto
    # --------------------------------------------------------------------
    # CharField: texto para la marca del producto.
    # max_length: hasta 55 caracteres.
    # validators: obliga a que la marca tenga al menos 4 letras.
    # verbose_name: etiqueta visible en formularios.
    # --------------------------------------------------------------------
    MarcaProducto = models.CharField(
        max_length=55,
        db_column='MarcaProducto',
        verbose_name="Marca",
        validators=[MinLengthValidator(4, message="La marca del producto debe tener al menos 4 caracteres")]
    )
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # FUNCIÓN: validacion_fecha_de_vencimiento_futura
    # --------------------------------------------------------------------
    # Esta función asegura que la fecha de vencimiento ingresada sea posterior
    # a la fecha actual. Si la fecha es anterior o igual a hoy, se lanza un error.
    # Esto previene el registro de productos ya vencidos.
    # --------------------------------------------------------------------
    def validacion_fecha_de_vencimiento_futura(value):
        if value <= timezone.now().date():
            raise ValidationError('La fecha ingresada no es una fecha futura.')
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # Fecha de vencimiento del producto
    # --------------------------------------------------------------------
    # DateField: almacena solo la fecha (sin hora).
    # validators: aplica la función anterior para evitar fechas pasadas o iguales a hoy.
    # verbose_name: etiqueta amigable para formularios y panel de administración.
    # --------------------------------------------------------------------
    FechaDeVencimiento = models.DateField(
        db_column='FechaDeVencimiento',
        verbose_name="Fecha de vencimiento",
        validators=[validacion_fecha_de_vencimiento_futura]
    )
    # --------------------------------------------------------------------

    ###LLAVE FORANEA###
    CategoriaProducto = models.ForeignKey(
        CategoriaProducto, #Modelo Relacionado
        on_delete=models.SET_NULL,
        related_name="producto", #Para acceder a el desde categoria
        db_column="CategoriaProductoId", #Nombre que tendra en la base de datos
        null=True, #Si puede quedar nulo
        blank=True #Si puede quedar vacio
        #SI NULL Y BLANK QUEDAN EN FALSE LA VALIDACION PERSONALIZADA QUEDA INACTIVA
    )
    #models.CASCADE → borra también el relacionado.
    #models.PROTECT → impide borrarlo si está en uso.
    #models.SET_NULL → pone NULL en la FK.
    #models.SET_DEFAULT → asigna valor por defecto

    #default="Sin valor", #Lo que ocurrre segun la lista de abajo si se elimina

    Bodegas = models.ForeignKey(
        Bodegas,
        on_delete=models.SET_NULL,
        related_name="producto",
        db_column="BodegaId",
        null=True,
        blank=True
    )


    # --------------------------------------------------------------------
    # Meta información del modelo
    # --------------------------------------------------------------------
    # La clase Meta se usa para definir configuraciones adicionales del modelo:
    #   - db_table: nombre exacto de la tabla en la base de datos.
    #   - constraints: establece reglas de unicidad para evitar duplicados.
    #     En este caso, ningún IdProducto ni CodigoDeBarras puede repetirse.
    # --------------------------------------------------------------------
    class Meta:
        db_table = 'Productos'
        constraints = [
            UniqueConstraint(fields=['IdProducto'], name='unique_id_producto'),
            UniqueConstraint(fields=['CodigoDeBarras'], name='unique_codigo_de_barras'),
        ]
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # MÉTODO __STR__ IMPLEMENTADO
    # --------------------------------------------------------------------
    # Este método define cómo se mostrará un objeto Producto cuando se imprima.
    # Se utiliza principalmente en el panel de administración o en consola.
    # Devuelve una cadena legible con la información principal del producto.
    # --------------------------------------------------------------------
    def __str__(self):
        return f"ID: {self.IdProducto}, NOMBRE: {self.NombreProducto}, CODIGO DE BARRAS: {self.CodigoDeBarras}, VALOR: {self.ValorProducto}, STOCK: {self.StockProducto}, MARCA: {self.MarcaProducto}, FECHA DE REGISTRO: {self.FechaDeRegistroProducto}, FECHA DE VENCIMIENTO: {self.FechaDeVencimiento}, CATEGORIA PRODUCTO: {self.CategoriaProducto}, BODEGA ASOCIADA: {self.Bodegas}"
    

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

    UserAuth = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        related_name="userAuthId", #Para acceder a el desde categoria
        db_column="superUserAsociado", #Nombre que tendra en la base de datos
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

#MANEJO DE AUDITORIAS A BODEGA
class AuditoriaBodega(models.Model):

    # Campo autoincremental que funciona como llave primaria
    IdAuditoriaBodega = models.AutoField(
        primary_key=True,
        db_column='IdAuditoriaBodega'
    )

    # Llave foránea hacia Bodega
    Bodega = models.ForeignKey(
        Bodegas,
        on_delete=models.SET_NULL,
        related_name='auditorias_bodegas',
        db_column="BodegaId",
        null=True,
        blank=True
    )

    # Llave foránea hacia Usuario que realizó la acción
    Usuario = models.ForeignKey(
        Usuarios,
        on_delete=models.SET_NULL, #EVITA QUE AL BORRAR UN USUARIO, SU FK EN LA AUDITORIA QUEDE NULL
        related_name='auditorias_bodega_usuario',
        db_column="UsuarioId",
        null=True,
        blank=True
    )
    
    # Campos de respaldo en caso de que la bodega sea eliminada o modificada
    BodegaIdRespaldo = models.IntegerField(
        null=True,
        blank=True
    )

    # Campos de respaldo en caso de que la bodega sea eliminada o modificada
    BodegaNombreRespaldo = models.CharField(
        max_length=70,
        null=True,
        blank=True
    )

    # Tipo de acción registrada en la auditoría
    Accion = models.CharField(
        max_length=50,
        choices=[
            ('CREAR', 'Crear'),
            ('ACTUALIZAR', 'Actualizar'),
            ('ELIMINAR', 'Eliminar'),
            ('MOVIMIENTO', 'Movimiento de stock')
        ]
    )

    # Tipo de acción registrada en la auditoría
    Fecha_hora = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'AuditoriaBodega'
        constraints = [
            UniqueConstraint(fields=['IdAuditoriaBodega'], name='unique_id_auditoria_bodega'),
        ]

    # Nombre exacto de la tabla en la base de datos
    def __str__(self):
        return f"ID: {self.IdAuditoriaBodega}, Bodega: {self.Bodega}, Nombre Bodega: {self.BodegaNombreRespaldo}, Usuario: {self.Usuario}, Accion: {self.Accion}, Fecha: {self.Fecha_hora}"
    

#-----------------------------------------------------------------------------------------------------------------------------------#
class AuditoriaCargo(models.Model):

    IdAuditoriaCargo = models.AutoField(
        primary_key=True,
        db_column='IdAuditoriaCargo'
    )

    # Llave foránea hacia Bodega
    Cargo = models.ForeignKey(
        Cargos,
        on_delete=models.SET_NULL,
        related_name='auditorias_cargos',
        db_column="CargoId",
        null=True,
        blank=True
    )

    # Llave foránea hacia Usuario que realizó la acción
    Usuario = models.ForeignKey(
        Usuarios,
        on_delete=models.SET_NULL, #EVITA QUE AL BORRAR UN USUARIO, SU FK EN LA AUDITORIA QUEDE NULL
        related_name='auditorias_cargo_usuario',
        db_column="UsuarioId",
        null=True,
        blank=True
    )

    # Datos de respaldo en caso de eliminación
    CargoIdRespaldo = models.IntegerField(
        null=True,
        blank=True
    )
    
    # Datos de respaldo en caso de eliminación
    CargoNombreRespaldo = models.CharField(
        max_length=70,
        null=True,
        blank=True
    )

    # Información de auditoría
    Accion = models.CharField(
        max_length=50,
        choices=[
            ('CREAR', 'Crear'),
            ('ACTUALIZAR', 'Actualizar'),
            ('ELIMINAR', 'Eliminar'),
            ('MOVIMIENTO', 'Movimiento de stock')
        ]
    )

    Fecha_hora = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'AuditoriaCargo'
        constraints = [
            UniqueConstraint(fields=['IdAuditoriaCargo'], name='unique_id_auditoria_cargo'),
        ]


    def __str__(self):
        return f"ID: {self.IdAuditoriaCargo}, Cargo: {self.Cargo}, Nombre Cargo: {self.CargoNombreRespaldo}, Usuario: {self.Usuario}, Accion: {self.Accion}, Fecha: {self.Fecha_hora}"
#-----------------------------------------------------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------------------------------------------------#
class AuditoriaCategoria(models.Model):

    IdAuditoriaCategoria = models.AutoField(
        primary_key=True,
        db_column='IdAuditoriaCategoria'
    )

    # Llave foránea hacia Bodega
    Categoria = models.ForeignKey(
        CategoriaProducto,
        on_delete=models.SET_NULL,
        related_name='auditorias_categoria',
        db_column="CategoriaId",
        null=True,
        blank=True
    )

    # Llave foránea hacia Usuario que realizó la acción
    Usuario = models.ForeignKey(
        Usuarios,
        on_delete=models.SET_NULL, #EVITA QUE AL BORRAR UN USUARIO, SU FK EN LA AUDITORIA QUEDE NULL
        related_name='auditorias_categoria_usuario',
        db_column="UsuarioId",
        null=True,
        blank=True
    )

    CategoriaIdRespaldo = models.IntegerField(
        null=True,
        blank=True
    )

    CategoriaNombreRespaldo = models.CharField(
        max_length=70,
        null=True,
        blank=True
    )

    # Información de auditoría
    Accion = models.CharField(
        max_length=50,
        choices=[
            ('CREAR', 'Crear'),
            ('ACTUALIZAR', 'Actualizar'),
            ('ELIMINAR', 'Eliminar'),
            ('MOVIMIENTO', 'Movimiento de stock')
        ]
    )

    Fecha_hora = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'AuditoriaCategoria'
        constraints = [
            UniqueConstraint(fields=['IdAuditoriaCategoria'], name='unique_id_auditoria_categoria'),
        ]


    def __str__(self):
        return f"ID: {self.IdAuditoriaCategoria}, Categoria: {self.Categoria}, Nombre Categoria: {self.CategoriaNombreRespaldo}, Usuario: {self.Usuario}, Accion: {self.Accion}, Fecha: {self.Fecha_hora}"
#-----------------------------------------------------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------------------------------------------------#
class AuditoriaEmpleado(models.Model):

    IdAuditoriaEmpleado = models.AutoField(
        primary_key=True,
        db_column='IdAuditoriaEmpleado'
    )

    # Llave foránea hacia Bodega
    Empleado = models.ForeignKey(
        Empleados,
        on_delete=models.SET_NULL,
        related_name='auditorias_empleado',
        db_column="EmpleadoId",
        null=True,
        blank=True
    )

    # Llave foránea hacia Usuario que realizó la acción
    Usuario = models.ForeignKey(
        Usuarios,
        on_delete=models.SET_NULL, #EVITA QUE AL BORRAR UN USUARIO, SU FK EN LA AUDITORIA QUEDE NULL
        related_name='auditorias_empleado_usuario',
        db_column="UsuarioId",
        null=True,
        blank=True
    )

    EmpleadoIdRespaldo = models.IntegerField(
        null=True,
        blank=True
    )

    EmpleadoNombreRespaldo = models.CharField(
        max_length=70,
        null=True,
        blank=True
    )

    # Información de auditoría
    Accion = models.CharField(
        max_length=50,
        choices=[
            ('CREAR', 'Crear'),
            ('ACTUALIZAR', 'Actualizar'),
            ('ELIMINAR', 'Eliminar'),
            ('MOVIMIENTO', 'Movimiento de stock')
        ]
    )

    Fecha_hora = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'AuditoriaEmpleado'
        constraints = [
            UniqueConstraint(fields=['IdAuditoriaEmpleado'], name='unique_id_auditoria_empleado'),
        ]


    def __str__(self):
        return f"ID: {self.IdAuditoriaEmpleado}, Empleado: {self.Empleado}, Nombre Empleado: {self.EmpleadoNombreRespaldo}, Usuario: {self.Usuario}, Accion: {self.Accion}, Fecha: {self.Fecha_hora}"
#-----------------------------------------------------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------------------------------------------------#
class AuditoriaProducto(models.Model):

    IdAuditoriaProducto = models.AutoField(
        primary_key=True,
        db_column='IdAuditoriaProducto'
    )

    # Llave foránea hacia Bodega
    Producto = models.ForeignKey(
        Productos,
        on_delete=models.SET_NULL,
        related_name='auditorias_producto',
        db_column="ProductoId",
        null=True,
        blank=True
    )

    # Llave foránea hacia Usuario que realizó la acción
    Usuario = models.ForeignKey(
        Usuarios,
        on_delete=models.SET_NULL, #EVITA QUE AL BORRAR UN USUARIO, SU FK EN LA AUDITORIA QUEDE NULL
        related_name='auditorias_producto_usuario',
        db_column="UsuarioId",
        null=True,
        blank=True
    )

    ProductoIdRespaldo = models.IntegerField(
        null=True,
        blank=True
    )

    ProductoNombreRespaldo = models.CharField(
        max_length=70,
        null=True,
        blank=True
    )

    # Información de auditoría
    Accion = models.CharField(
        max_length=50,
        choices=[
            ('CREAR', 'Crear'),
            ('ACTUALIZAR', 'Actualizar'),
            ('ELIMINAR', 'Eliminar'),
            ('MOVIMIENTO', 'Movimiento de stock')
        ]
    )

    Fecha_hora = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'AuditoriaProducto'
        constraints = [
            UniqueConstraint(fields=['IdAuditoriaProducto'], name='unique_id_auditoria_producto'),
        ]


    def __str__(self):
        return f"ID: {self.IdAuditoriaProducto}, Producto: {self.Producto}, Nombre Producto: {self.ProductoNombreRespaldo}, Usuario: {self.Usuario}, Accion: {self.Accion}, Fecha: {self.Fecha_hora}"
#-----------------------------------------------------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------------------------------------------------#
class AuditoriaUsuario(models.Model):

    IdAuditoriaUsuario = models.AutoField(
        primary_key=True,
        db_column='IdAuditoriaUsuario'
    )

    # Llave foránea hacia Usuario que realizó la acción
    Usuario = models.ForeignKey(
        Usuarios,
        on_delete=models.SET_NULL, #EVITA QUE AL BORRAR UN USUARIO, SU FK EN LA AUDITORIA QUEDE NULL
        related_name='auditorias_usuario_usuario',
        db_column="UsuarioId",
        null=True,
        blank=True
    )

    UsuarioIdRespaldo = models.IntegerField(
        null=True,
        blank=True
    )

    UsuarioNombreRespaldo = models.CharField(
        max_length=70,
        null=True,
        blank=True
    )

    # Información de auditoría
    Accion = models.CharField(
        max_length=50,
        choices=[
            ('CREAR', 'Crear'),
            ('ACTUALIZAR', 'Actualizar'),
            ('ELIMINAR', 'Eliminar'),
            ('MOVIMIENTO', 'Movimiento de stock')
        ]
    )

    Fecha_hora = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'AuditoriaUsuario'
        constraints = [
            UniqueConstraint(fields=['IdAuditoriaUsuario'], name='unique_id_auditoria_usuario'),
        ]


    def __str__(self):
        return f"ID: {self.IdAuditoriaUsuario},  Usuario: {self.Usuario}, Nombre Usuario: {self.UsuarioNombreRespaldo}, Accion: {self.Accion}, Fecha: {self.Fecha_hora}"
#-----------------------------------------------------------------------------------------------------------------------------------#