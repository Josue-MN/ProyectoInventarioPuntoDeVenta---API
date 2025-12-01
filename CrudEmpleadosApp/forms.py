# Importaciones necesarias
from django import forms  # Importa el módulo de formularios de Django
from CrudEmpleadosApp.models import Empleados  # Importa el modelo Empleados
import re

# ========================================================================
# Formulario: Registro de Empleados
# ========================================================================
# Este formulario permite crear o actualizar registros de empleados
# usando el modelo Empleados. Se basa en ModelForm, por lo que
# automáticamente genera campos según el modelo.
# ========================================================================

# Formulario para registrar o actualizar empleados
class EmpleadoRegistrationForm(forms.ModelForm):

    """
    Formulario basado en el modelo Empleados.
    Permite crear o actualizar empleados desde un formulario HTML.
    """

    class Meta:
        model = Empleados  # Modelo asociado al formulario
        fields = '__all__'  # Incluye todos los campos del modelo

        # Etiquetas para mostrar en los formularios
        labels = {
            'RutEmpleado': 'Rut del empleado',
            'NombreEmpleado': 'Nombre',
            'ApellidoEmpleado': 'Apellido',
            'EdadEmpleado': 'Edad',
            'NumeroTelefonoEmpleado': 'Numero telefonico',
            'Empleado': 'Empleado Seleccionado',
            'Cargo': 'Cargo Seleccionado'
        }

        # Ayudas que se muestran como hint en los campos
        help_texts = {
            'RutEmpleado': 'Indique el rut del empleado a registrar',
            'NombreEmpleado': 'Indique el nombre del empleado',
            'ApellidoEmpleado': 'Indique el apellido del empleado',
            'EdadEmpleado': 'Ingrese la edad del empleado',
            'NumeroTelefonoEmpleado': 'Ingrese el numero telefonico del empleado',
            'Empleado': 'Eliga un Empleado',
            'Cargo': 'Eliga un Cargo'
        }

        # Mensajes de error personalizados
        error_messages = {
            'RutEmpleado': {
                'required': 'Por favor introduzca el rut',
                'unique': 'Este rut ya esta registrado',
                'invalid': 'Ingrese un rut valido (01234567-k) con guion y sin puntos.',
            },
            'NombreEmpleado': {
                'required': 'Por favor introduzca el nombre del empleado',
            },
            'ApellidoEmpleado': {
                'required': 'Por favor introduzca el apellido del empleado',
            },
            'EdadEmpleado': {
                'required': 'Por favor introduzca la edad del empleado',
                'invalid': 'Ingrese una edad valida',
            },
            'NumeroTelefonoEmpleado': {
                'required': 'Por favor introduzca un numero telefonico',
                'invalid': 'Ingrese un numero telefonico valido (912345678)',
            },
        }

        # Widgets personalizados para cada campo
        widgets = {
            'RutEmpleado': forms.TextInput(attrs={'placeholder': 'Ej: (01234567-k)'}),
            'NombreEmpleado': forms.TextInput(attrs={'placeholder': 'Ej: Pablo'}),
            'ApellidoEmpleado': forms.TextInput(attrs={'placeholder': 'Ej: Campusano Sotomayor'}),
            'EdadEmpleado': forms.NumberInput(attrs={'placeholder': 'Ej: 20 (años)'}),
            'NumeroTelefonoEmpleado': forms.NumberInput(attrs={'placeholder': 'Ej: (912345678)'}),
        }

    # ====================================================================
    # Validaciones personalizadas
    # ====================================================================

    # Valida que el RUT tenga el formato correcto y no esté duplicado
    def clean_RutEmpleado(self):
        inputRut = self.cleaned_data['RutEmpleado'].strip().upper()  # Limpia espacios y convierte a mayúscula
        caracteres = r"^\d{7,8}-[\dK]$"  # Expresión regular para validar el RUT
        query = Empleados.objects.filter(RutEmpleado=inputRut)  # Verifica duplicados

        # Si es actualización, excluye el propio registro
        if self.instance.pk:
            query = query.exclude(pk=self.instance.pk)

        # Valida formato del RUT
        if not re.match(caracteres, inputRut):
            raise forms.ValidationError("Ingrese un Rut Valido con guion y sin puntos.")

        # Valida duplicados
        if query.exists():
            raise forms.ValidationError("Este RUT ya está registrado.")

        return inputRut  # Retorna valor limpio si es válido

    # Valida que el nombre solo contenga letras y mínimo 3 caracteres
    def clean_NombreEmpleado(self):
        inputNombre = self.cleaned_data['NombreEmpleado'].strip().capitalize()
        caracteres = r"^[A-ZÁÉÍÓÚÑa-záéíóúñ]{3,}$"

        if not re.match(caracteres, inputNombre):
            raise forms.ValidationError("Ingrese un Nombre valido con solo letras y sin espacios.")

        return inputNombre

    # Valida que el apellido solo contenga letras y un máximo de un espacio entre palabras
    def clean_ApellidoEmpleado(self):
        inputApellido = self.cleaned_data['ApellidoEmpleado'].strip().title()
        caracteres = r"^([A-ZÁÉÍÓÚÑa-záéíóúñ]{2,})( [A-ZÁÉÍÓÚÑa-záéíóúñ]{2,})*$"

        if not re.match(caracteres, inputApellido):
            raise forms.ValidationError("Ingrese un Apellido valido con solo letras.")

        return inputApellido

    # Valida que la edad sea entre 18 y 100
    def clean_EdadEmpleado(self):
        inputedad = self.cleaned_data['EdadEmpleado']

        if inputedad < 0:
            raise forms.ValidationError("No ingrese numeros negativos.")
        if inputedad < 18:
            raise forms.ValidationError("La edad debe ser mayor o igual a 18 años.")
        if inputedad > 100:
            raise forms.ValidationError("La edad no puede ser mayor a 100 años.")

        return inputedad

    # Valida que el número telefónico tenga 9 dígitos y comience con 9
    def clean_NumeroTelefonoEmpleado(self):
        inputtelefono = str(self.cleaned_data['NumeroTelefonoEmpleado']).strip()
        caracteres = r"^9\d{8}$"

        if not re.match(caracteres, inputtelefono):
            raise forms.ValidationError("Ingrese un numero de solo 9 digitos, anteponiendo el nueve.")

        return inputtelefono
