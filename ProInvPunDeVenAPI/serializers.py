from rest_framework import serializers
from ProInvPunDeVenAPI.models import *
import re
from datetime import date
from django.contrib.auth.hashers import make_password

class BodegasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bodegas
        fields = '__all__'
        extra_kwargs = {
            "NombreBodega": {
                "help_text": "ejemplo: Bodega luz"
            },
            "UbicacionBodega": {
                "help_text": "ejemplo: Area norte"
            },
            "EstadoBodega": {
                "help_text": "ejemplo: Activo"
            },
            "ObservacionesBodega": {
                "help_text": "ejemplo: Esta bodega esta destinada a mercaderia del oasis"
            }
        }

    # ---------------------------
    # VALIDACIONES PERSONALIZADAS
    # ---------------------------

    def validate_NombreBodega(self, value):
        """
        Limpia y valida el campo 'NombreBodega'.
        - Elimina espacios innecesarios.
        - Convierte el texto a formato Título (primera letra mayúscula).
        - Verifica que solo contenga letras, números o espacios válidos.
        """
        valueNombreBodega = value.strip().title()

        # Expresión regular: permite letras y números, pero no mezcla de ambos sin espacio
        caracteres = r"^(?:\d+|[A-ZÁÉÍÓÚÑa-záéíóúñ]{2,})(?: (?:\d+|[A-ZÁÉÍÓÚÑa-záéíóúñ]{2,}))*$"

        # Si el texto no cumple con el patrón, muestra error
        if not re.match(caracteres, valueNombreBodega):
            raise serializers.ValidationError(
                "Ingrese un nombre de bodega sin caracteres especiales, "
                "con más de 5 letras, sin juntar números ni letras y sin más de un espacio entre palabras."
            )
        return valueNombreBodega  # Devuelve el valor limpio si es válido

    def validate_UbicacionBodega(self, value):
        """
        Limpia y valida el campo 'UbicacionBodega'.
        - Elimina espacios.
        - Convierte a formato Título.
        - Valida caracteres permitidos.
        """
        valueUbicacionBodega = value.strip().title()
        caracteres = r"^(?:\d+|[A-ZÁÉÍÓÚÑa-záéíóúñ]{2,})(?: (?:\d+|[A-ZÁÉÍÓÚÑa-záéíóúñ]{2,}))*$"

        if not re.match(caracteres, valueUbicacionBodega):
            raise serializers.ValidationError(
                "Ingrese la ubicación de la bodega sin caracteres especiales, "
                "con más de 5 letras, sin juntar números ni letras y sin más de un espacio entre palabras."
            )
        return valueUbicacionBodega

    def validate_ObservacionesBodega(self, value):
        """
        Valida el campo 'ObservacionesBodega'.
        - Debe tener al menos 10 caracteres.
        - No puede contener solo números.
        """
        valueObservacionesBodega = value

        # Longitud mínima
        if len(valueObservacionesBodega) < 10:
            raise serializers.ValidationError("La observación debe tener al menos 10 caracteres.")
        
        # No permitir solo números
        if valueObservacionesBodega.isdigit():
            raise serializers.ValidationError("La observación no puede contener solo números.")
        
        return valueObservacionesBodega

class CargosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargos
        fields = '__all__'
        extra_kwargs = {
            "TipoDeCargo": {
                "help_text": "ejemplo: Bodeguero"
            },
            "EstadoDelCargo": {
                "help_text": "ejemplo: Activo"
            },
            "DescripcionDelCargo": {
                "help_text": "ejemplo: este cargo de bodeguero se encarga de almacenar"
            },
            "SueldoBase": {
                "help_text": "ejemplo: 500000"
            }
        }


    # --- VALIDACIONES PERSONALIZADAS ---
    
    # Valida que la descripción tenga al menos 10 caracteres
    def validate_DescripcionDelCargo(self, value):
        valueDescripcionDelCargo = value.strip()
        if len(valueDescripcionDelCargo) < 10:
            raise serializers.ValidationError("La descripción del cargo debe tener al menos 10 caracteres")
        if valueDescripcionDelCargo.isdigit():
            raise serializers.ValidationError("La descripción no puede contener solo números")
        return valueDescripcionDelCargo
    
    # Valida que el sueldo base sea positivo
    def validate_SueldoBase(self, value):
        valueSueldoBase = value
        if valueSueldoBase <= 0:
            raise serializers.ValidationError("El sueldo base debe ser mayor a 0")
        return valueSueldoBase


class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = '__all__'
        extra_kwargs = {
            "NombreCategoria": {
                "help_text": "ejemplo: Jugos"
            },
            "Descripcion": {
                "help_text": "ejemplo: Esta categoria almacena jugos"
            },
            "Estado": {
                "help_text": "ejemplo: Activa"
            },
            "Observaciones": {
                "help_text": "ejemplo: Se neceesita almacenar los jugos por seccion"
            }
        }

    # Validación personalizada para el campo NombreCategoria
    def validate_NombreCategoria(self, value):
        valueNombre = value  # Obtiene el valor del campo
        if len(valueNombre) < 3:  # Valida que tenga al menos 3 caracteres
            raise serializers.ValidationError("El largo del nombre de la categoria debe ser mas de 3 caracteres")
        return valueNombre  # Retorna el valor limpio si es válido
    
    # Validación personalizada para el campo Descripcion
    def validate_Descripcion(self, value):
        valueDescripcion = value.strip()  # Elimina espacios al inicio y fin
        if len(valueDescripcion) < 10:  # Valida longitud mínima
            raise serializers.ValidationError("La descripción debe tener al menos 10 caracteres.")
        return valueDescripcion  # Retorna el valor limpio si es válido

    # Validación personalizada para el campo Observaciones
    def validate_Observaciones(self, value):
        valueObservaciones = value.strip()  # Elimina espacios al inicio y fin
        if len(valueObservaciones) < 10:  # Valida longitud mínima
            raise serializers.ValidationError("Las observaciones deben tener al menos 10 caracteres.")
        return valueObservaciones  # Retorna el valor limpio si es válido

class EmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = '__all__'
        extra_kwargs = {
            "RutEmpleado": {
                "help_text": "ejemplo: Bodeguero"
            },
            "NombreEmpleado": {
                "help_text": "ejemplo: Activo"
            },
            "ApellidoEmpleado": {
                "help_text": "ejemplo: este cargo de bodeguero se encarga de almacenar"
            },
            "EdadEmpleado": {
                "help_text": "ejemplo: 500000"
            },
            "NumeroTelefonoEmpleado": {
                "help_text": "ejemplo: 12345678"
            },
        }

    # ====================================================================
    # Validaciones personalizadas
    # ====================================================================

    # Valida que el RUT tenga el formato correcto y no esté duplicado
    def validate_RutEmpleado(self, value):
        valueRut = value.strip().upper()  # Limpia espacios y convierte a mayúscula
        caracteres = r"^\d{7,8}-[\dK]$"  # Expresión regular para validar el RUT
        query = Empleados.objects.filter(RutEmpleado=valueRut)  # Verifica duplicados

        # Si es actualización, excluye el propio registro
        if self.instance:
            query = query.exclude(pk=self.instance.pk)

        # Valida formato del RUT
        if not re.match(caracteres, valueRut):
            raise serializers.ValidationError("Ingrese un Rut Valido con guion y sin puntos.")

        # Valida duplicados
        if query.exists():
            raise serializers.ValidationError("Este RUT ya está registrado.")

        return valueRut  # Retorna valor limpio si es válido

    # Valida que el nombre solo contenga letras y mínimo 3 caracteres
    def validate_NombreEmpleado(self, value):
        valueNombre = value.strip().capitalize()
        caracteres = r"^[A-ZÁÉÍÓÚÑa-záéíóúñ]{3,}$"

        if not re.match(caracteres, valueNombre):
            raise serializers.ValidationError("Ingrese un Nombre valido con solo letras y sin espacios.")

        return valueNombre

    # Valida que el apellido solo contenga letras y un máximo de un espacio entre palabras
    def validate_ApellidoEmpleado(self, value):
        valueApellido = value.strip().title()
        caracteres = r"^([A-ZÁÉÍÓÚÑa-záéíóúñ]{2,})( [A-ZÁÉÍÓÚÑa-záéíóúñ]{2,})*$"

        if not re.match(caracteres, valueApellido):
            raise serializers.ValidationError("Ingrese un Apellido valido con solo letras.")

        return valueApellido

    # Valida que la edad sea entre 18 y 100
    def validate_EdadEmpleado(self, value):
        valueedad = value
        
        if valueedad < 0:
            raise serializers.ValidationError("No ingrese numeros negativos.")
        if valueedad < 18:
            raise serializers.ValidationError("La edad debe ser mayor o igual a 18 años.")
        if valueedad > 100:
            raise serializers.ValidationError("La edad no puede ser mayor a 100 años.")

        return valueedad

    # Valida que el número telefónico tenga 9 dígitos y comience con 9
    def validate_NumeroTelefonoEmpleado(self, value):
        valuetelefono = str(value).strip()
        caracteres = r"^9\d{8}$"

        if not re.match(caracteres, valuetelefono):
            raise serializers.ValidationError("Ingrese un numero de solo 9 digitos, anteponiendo el nueve.")

        return valuetelefono


class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'
        extra_kwargs = {
            "CodigoDeBarras": {
                "help_text": "ejemplo: 121212121212"
            },
            "ValorProducto": {
                "help_text": "ejemplo: 10000"
            },
            "StockProducto": {
                "help_text": "ejemplo: 10"
            },
            "NombreProducto": {
                "help_text": "ejemplo: Bebida Juan"
            },
            "MarcaProducto": {
                "help_text": "ejemplo: Bills & Paps"
            },
            "FechaDeVencimiento": {
                "help_text": "ejemplo: 12/12/2050"
            },

        }


    # ====================================================================
    # Validaciones personalizadas por campo
    # ====================================================================

    # Valida que el código de barras sea solo números y único
    def validate_CodigoDeBarras(self, value):
        valueCodigoDeBarras = value
        expresion = r'^[0-9]+$'
        query = Productos.objects.filter(CodigoDeBarras=valueCodigoDeBarras)

        if not re.match(expresion, valueCodigoDeBarras):
            raise serializers.ValidationError("Ingrese solamente numeros y sin espacios")
        if self.instance:
            query = query.exclude(pk=self.instance.pk)  # Excluye el registro actual si es edición
        if query.exists():
            raise serializers.ValidationError("Este Codigo de Barras ya está registrado.")
        return valueCodigoDeBarras

    # Valida que el valor del producto sea positivo y mínimo 3 dígitos
    def validate_ValorProducto(self, value):
        valueValorProducto = value

        if valueValorProducto < 0:
            raise serializers.ValidationError("No puede ingresar valores negativos")
        if len(str(valueValorProducto)) < 3:
            raise serializers.ValidationError("Debe ingresar un valor valido a partir de 3 digitos ($123)")
        if valueValorProducto == 0:
            raise serializers.ValidationError("El valor no puede ser 0")
        return valueValorProducto

    # Valida que el stock sea positivo y mayor a 0
    def validate_StockProducto(self, value):
        valueStockProducto = value

        if valueStockProducto < 0:
            raise serializers.ValidationError("No puede ingresar stock negativos")
        if valueStockProducto == 0:
            raise serializers.ValidationError("El Stock no puede ser 0")
        return valueStockProducto

    # Valida que el nombre del producto no contenga caracteres especiales y tenga formato correcto
    def validate_NombreProducto(self, value):
        valueNombreProducto = value.strip()
        caracteres = r'^[A-Za-zÁÉÍÓÚÑáéíóúñ]+(?: [A-Za-zÁÉÍÓÚÑáéíóúñ]+)*(?: \d+[gG]?)?$'

        if not re.match(caracteres, valueNombreProducto):
            raise serializers.ValidationError(
                "Ingrese un nombre del producto sin caracteres especiales, con de mas de 5 letras, "
                "sin juntar numeros ni letras y no con mas de 1 espacio entre caracteres."
            )
        return valueNombreProducto

    # Valida que la fecha de vencimiento sea posterior a la fecha actual
    def validate_FechaDeVencimiento(self, value):
        valueFechaDeVencimiento = value

        if not valueFechaDeVencimiento:
            raise serializers.ValidationError("Debe ingresar una fecha de vencimiento.")
        
        fecha_actual = date.today()
        if valueFechaDeVencimiento < fecha_actual:
            raise serializers.ValidationError("La fecha de vencimiento no puede ser anterior a la fecha actual.")

        return valueFechaDeVencimiento
    

    ##SE ESPECIFICA QUE SERA UNA PRIMARY KEY (PrimaryKeyRelatedField) Y NO UN OBJECTO COMPLETO
    ##QUERYSET HACE LA RELACION DE DONDE SE SACARA LA PRIMARY KEY EXISTENTE
    ##REQUIERED HACE QUE ESTE CAMPO SEA OBLIGATORIOI SI O SI
    ##ALLOW_NULL=FALSE ESPECIFICA QUE NO PUEDE QUEDAR NULO
    CategoriaProducto = serializers.PrimaryKeyRelatedField(
        queryset=CategoriaProducto.objects.all(),
        help_text="ejemplo: 1",
        required=True,
        allow_null=False
    )

    ##SE ESPECIFICA QUE SERA UNA PRIMARY KEY (PrimaryKeyRelatedField) Y NO UN OBJECTO COMPLETO
    ##QUERYSET HACE LA RELACION DE DONDE SE SACARA LA PRIMARY KEY EXISTENTE
    ##REQUIERED HACE QUE ESTE CAMPO SEA OBLIGATORIOI SI O SI
    ##ALLOW_NULL=FALSE ESPECIFICA QUE NO PUEDE QUEDAR NULO
    Bodegas = serializers.PrimaryKeyRelatedField(
        queryset=Bodegas.objects.all(),
        help_text="ejemplo: 1",
        required=True,
        allow_null=False
    )

    ###VALIDACION FOREIGN KEY CATEGORIA
    def validate_CategoriaProducto(self, value):
        # Obtiene la categoría seleccionada
        ExisteCategoriaProducto = value
        # Si no existen categorías registradas en la BD
        if ExisteCategoriaProducto is None:
            raise serializers.ValidationError("Debes seleccionar una categoría de producto.")
        # Retorna la categoría válida
        return ExisteCategoriaProducto

    ###VALIDACION FOREIGN KEY BODEGA
    def validate_Bodegas(self, value):
        # Obtiene la categoría seleccionada
        ExisteBodegas = value
        # Si el usuario no seleccionó ninguna bodega
        if ExisteBodegas is None:
            raise serializers.ValidationError("Debes seleccionar una bodega para el producto.")
        # Retorna la categoría válida
        return ExisteBodegas
    

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'
        extra_kwargs = {
            "Username": {
                "help_text": "ejemplo: Juaneswt"
            },
            "Password": {
                "help_text": "ejemplo: hola.33"
            },
            "CorreoElectronico": {
                "help_text": "ejemplo: juanes@gmail.com"
            },
        }
        #Hace que muestre todos los datos del modelo asociado con OneToOne en el modelo usuario de userauth
        depth = 1

    
    # =============================================================================
    # VALIDACIÓN DE USERNAME
    # =============================================================================
    def validate_Username(self, value):
        valueUsername = value.lower().strip()
        patron = r'^[A-Za-z0-9_-]{5,}$'
        query = Usuarios.objects.filter(Username=valueUsername)

        if not re.match(patron, valueUsername):
            raise serializers.ValidationError(
                "Debe tener mínimo 5 caracteres y solo letras, números, '-' o '_'."
            )
        if valueUsername.isdigit():
            raise serializers.ValidationError("El nombre no puede ser solo números.")
        # Si es actualización, excluir su propio registro
        if self.instance:
            query = query.exclude(pk=self.instance.pk)
        if query.exists():
            raise serializers.ValidationError("Este usuario ya existe.")

        return valueUsername


    # =============================================================================
    # VALIDACIÓN DE PASSWORD
    # =============================================================================
    def validate_Password(self, value):
        valuePassword = value.strip()
        patron = r'^(?=.*[A-Za-z])(?=.*\d).{5,}$'

        if not re.match(patron, valuePassword):
            raise serializers.ValidationError(
                "La contraseña debe tener al menos 5 caracteres, 1 letra y 1 número."
            )

        return make_password(valuePassword)

    # =============================================================================
    # VALIDACIÓN DE FOREIGN KEYS — EMPLEADO
    # =============================================================================
    ##SE ESPECIFICA QUE SERA UNA PRIMARY KEY (PrimaryKeyRelatedField) Y NO UN OBJECTO COMPLETO
    ##QUERYSET HACE LA RELACION DE DONDE SE SACARA LA PRIMARY KEY EXISTENTE
    ##REQUIERED HACE QUE ESTE CAMPO SEA OBLIGATORIOI SI O SI
    ##ALLOW_NULL=FALSE ESPECIFICA QUE NO PUEDE QUEDAR NULO
    Empleado = serializers.PrimaryKeyRelatedField(
        queryset=Empleados.objects.all(),
        help_text="ejemplo: 1",
        required=True,
        allow_null=False
    )
    def validate_Empleado(self, value):
        empleado = value
        query = Usuarios.objects.filter(Empleado=empleado)

        if self.instance:
            query = query.exclude(pk=self.instance.pk)

        if query.exists():
            raise serializers.ValidationError("Este empleado ya está asignado a un usuario.")

        if empleado is None:
            raise serializers.ValidationError("Debe seleccionar un empleado.")

        return empleado


    ##SE ESPECIFICA QUE SERA UNA PRIMARY KEY (PrimaryKeyRelatedField) Y NO UN OBJECTO COMPLETO
    ##QUERYSET HACE LA RELACION DE DONDE SE SACARA LA PRIMARY KEY EXISTENTE
    ##REQUIERED HACE QUE ESTE CAMPO SEA OBLIGATORIOI SI O SI
    ##ALLOW_NULL=FALSE ESPECIFICA QUE NO PUEDE QUEDAR NULO
    Cargo = serializers.PrimaryKeyRelatedField(
        queryset=Cargos.objects.all(),
        help_text="ejemplo: 1",
        required=True,
        allow_null=False
    )
    # =============================================================================
    # VALIDACIÓN DE FOREIGN KEYS — CARGO
    # =============================================================================
    def validate_Cargo(self, value):
        cargo = value

        if cargo is None:
            raise serializers.ValidationError("Debe seleccionar un cargo.")

        return cargo
    



    UserAuth = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        help_text="ejemplo: 1",
        required=True,
        allow_null=False
    )
    def validate_UserAuth(self, value):
        userAuth = value
        query = Usuarios.objects.filter(UserAuth=userAuth)

        if self.instance:
            query = query.exclude(pk=self.instance.pk)

        if query.exists():
            raise serializers.ValidationError("Este empleado ya está asignado a un usuario.")

        if userAuth is None:
            raise serializers.ValidationError("Debe seleccionar un super usuario asociado.")

        return userAuth



class AuditoriasBodegasSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditoriaBodega
        fields = '__all__'

class AuditoriasCargosSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditoriaCargo
        fields = '__all__'

class AuditoriasCategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditoriaCategoria
        fields = '__all__'

class AuditoriasEmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditoriaEmpleado
        fields = '__all__'

class AuditoriasProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditoriaProducto
        fields = '__all__'

class AuditoriasUsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditoriaUsuario
        fields = '__all__'