from django import forms
from CrudUsuariosApp.models import Usuarios
import re
from django.contrib.auth.hashers import make_password
from CrudEmpleadosApp.models import Empleados
from CrudCargosApp.models import Cargos


# =============================================================================
# FORMULARIO DE REGISTRO DE USUARIOS (UsuarioRegistrationForm)
# =============================================================================
# Este formulario se utiliza para CREAR usuarios nuevos.
# Incluye campos personalizados, validaciones avanzadas y manejo de llaves foráneas.
# =============================================================================

class UsuarioRegistrationForm(forms.ModelForm):

    # Campo extra (NO existe en la BD). Solo se usa para validar la contraseña.
    ConfirmarPassword = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Repita su contraseña'}),
        label="Confirmar contraseña"
    )

    # =============================================================================
    # CONFIGURACIÓN DE CAMPOS (class Meta)
    # =============================================================================
    class Meta:
        model = Usuarios
        fields = ['Username', 'CorreoElectronico', 'Empleado', 'Cargo', 'Password', 'ConfirmarPassword']

        labels = {
            'Username': 'Nombre de usuario',
            'Password': 'Contraseña',
            'ConfirmarPassword': 'Confirmar contraseña',
            'CorreoElectronico': 'Correo electrónico',
            'Empleado': 'Empleado seleccionado',
            'Cargo': 'Cargo seleccionado'
        }

        help_texts = {
            'Username': 'Ingrese un nombre de usuario válido.',
            'Password': 'Debe tener al menos 5 caracteres, 1 letra y 1 número.',
            'ConfirmarPassword': 'Repita la contraseña.',
            'CorreoElectronico': 'Ingrese un correo electrónico válido.',
            'Empleado': 'Seleccione un empleado existente.',
            'Cargo': 'Seleccione un cargo existente.'
        }

        error_messages = {
            'Username': {
                'required': 'Debe ingresar un nombre de usuario.',
                'unique': 'Este nombre de usuario ya existe.'
            },
            'CorreoElectronico': {
                'invalid': 'Debe ingresar un correo válido.',
                'unique': 'El correo ya está en uso.'
            }
        }

        widgets = {
            'Username': forms.TextInput(attrs={'placeholder': 'Ej: Pablo123'}),
            'Password': forms.PasswordInput(attrs={'placeholder': 'Ej: Pablo_68'}),
            'ConfirmarPassword': forms.PasswordInput(attrs={'placeholder': 'Repita su contraseña'}),
            'CorreoElectronico': forms.EmailInput(attrs={'placeholder': 'Ej: usuario@gmail.com'})
        }


    # =============================================================================
    # VALIDACIÓN DE USERNAME
    # =============================================================================
    def clean_Username(self):
        inputUsername = self.cleaned_data['Username']
        patron = r'^[A-Za-z0-9_-]{5,}$'
        query = Usuarios.objects.filter(Username=inputUsername)

        # Si es actualización, excluir su propio registro
        if self.instance.pk:
            query = query.exclude(pk=self.instance.pk)

        if not re.match(patron, inputUsername):
            raise forms.ValidationError(
                "Debe tener mínimo 5 caracteres y solo letras, números, '-' o '_'."
            )

        if inputUsername.isdigit():
            raise forms.ValidationError("El nombre no puede ser solo números.")

        if query.exists():
            raise forms.ValidationError("Este usuario ya existe.")

        return inputUsername


    # =============================================================================
    # VALIDACIÓN DE PASSWORD
    # =============================================================================
    def clean_Password(self):
        inputPassword = self.cleaned_data['Password'].strip()
        patron = r'^(?=.*[A-Za-z])(?=.*\d).{5,}$'

        if not re.match(patron, inputPassword):
            raise forms.ValidationError(
                "La contraseña debe tener al menos 5 caracteres, 1 letra y 1 número."
            )

        return inputPassword


    # =============================================================================
    # VALIDACIÓN GLOBAL DEL FORMULARIO
    # =============================================================================
    def clean(self):
        cleaned_data = super().clean()

        Password = cleaned_data.get("Password")
        ConfirmarPassword = cleaned_data.get("ConfirmarPassword")

        if Password != ConfirmarPassword:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        # Se hashea aquí para guardar en BD
        cleaned_data["Password"] = make_password(Password)

        return cleaned_data


    # =============================================================================
    # VALIDACIÓN DE FOREIGN KEYS — EMPLEADO
    # =============================================================================
    def clean_Empleado(self):
        empleado = self.cleaned_data.get('Empleado')
        query = Usuarios.objects.filter(Empleado=empleado)

        if not Empleados.objects.exists():
            raise forms.ValidationError("Debe registrar empleados primero.")

        if self.instance.pk:
            query = query.exclude(pk=self.instance.pk)

        if query.exists():
            raise forms.ValidationError("Este empleado ya está asignado a un usuario.")

        if empleado is None:
            raise forms.ValidationError("Debe seleccionar un empleado.")

        return empleado


    # =============================================================================
    # VALIDACIÓN DE FOREIGN KEYS — CARGO
    # =============================================================================
    def clean_Cargo(self):
        cargo = self.cleaned_data.get('Cargo')

        if not Cargos.objects.exists():
            raise forms.ValidationError("Debe registrar cargos primero.")

        if cargo is None:
            raise forms.ValidationError("Debe seleccionar un cargo.")

        return cargo


    # =============================================================================
    # CONFIGURACIÓN DINÁMICA DE CAMPOS (__init__)
    # =============================================================================
    # Este __init__ se ejecuta SIEMPRE que se crea el formulario (crear o actualizar).
    #
    # Se usa para configurar:
    #   - queryset: qué datos se muestran
    #   - label_from_instance: cómo se muestran los datos
    #   - empty_label: texto inicial del select
    #
    # Explicación de *args y **kwargs:
    #   *args      → argumentos posicionales (sin nombre)
    #   **kwargs   → argumentos con nombre (data, instance, initial, etc.)
    #
    # Es obligatorio manejarlos para no romper cómo Django construye el formulario.
    # =============================================================================
    def __init__(self, *args, **kwargs):

        # Construcción inicial estándar del ModelForm
        super().__init__(*args, **kwargs)

        # =========================================================================
        # CONFIGURAR SELECT 'Empleado'
        # =========================================================================
        self.fields['Empleado'].queryset = Empleados.objects.all()

        self.fields['Empleado'].label_from_instance = (
            lambda obj: f"{obj.NombreEmpleado} {obj.ApellidoEmpleado} - RUT: {obj.RutEmpleado}"
        )

        self.fields['Empleado'].empty_label = "Seleccione un empleado existente."

        # =========================================================================
        # CONFIGURAR SELECT 'Cargo'
        # =========================================================================
        self.fields['Cargo'].queryset = Cargos.objects.all()

        self.fields['Cargo'].label_from_instance = (
            lambda obj: f"{obj.TipoDeCargo} - {obj.DescripcionDelCargo}"
        )

        self.fields['Cargo'].empty_label = "Seleccione un cargo existente."
        



# =============================================================================
# FORMULARIO DE ACTUALIZACIÓN DE USUARIOS (UsuarioUpdateForm)
# =============================================================================
# Este formulario sirve para EDITAR un usuario existente.
# Incluye:
#   - Checkbox para decidir si cambiar contraseña
#   - Validaciones diferentes al formulario de registro
#   - Empleado bloqueado (no editable)
# =============================================================================

class UsuarioUpdateForm(forms.ModelForm):

    # Campos opcionales para cambiar password
    CambiarPassword = forms.BooleanField(required=False, label="Cambiar contraseña")
    Password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Nueva contraseña'}),
        required=False,
        label="Nueva contraseña"
    )
    ConfirmarPassword = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña'}),
        required=False,
        label="Confirmar contraseña"
    )

    class Meta:
        model = Usuarios
        fields = ['Username', 'CorreoElectronico', 'Empleado', 'Cargo']

        widgets = {
            'Username': forms.TextInput(attrs={'placeholder': 'Ej: Pablo123'}),
            'CorreoElectronico': forms.EmailInput(attrs={'placeholder': 'Ej: usuario@gmail.com'}),
        }


    # =============================================================================
    # VALIDACIÓN USERNAME
    # =============================================================================
    def clean_Username(self):
        username = self.cleaned_data['Username']
        patron = r'^[A-Za-z0-9_-]{5,}$'
        query = Usuarios.objects.filter(Username=username)

        if self.instance.pk:
            query = query.exclude(pk=self.instance.pk)

        if not re.match(patron, username):
            raise forms.ValidationError("Formato inválido para Username.")

        if query.exists():
            raise forms.ValidationError("Este nombre de usuario ya existe.")

        if username.isdigit():
            raise forms.ValidationError("No puede ser solo números.")

        return username


    # =============================================================================
    # VALIDACIÓN GLOBAL — CAMBIO DE CONTRASEÑA
    # =============================================================================
    def clean(self):
        cleaned_data = super().clean()

        cambiar = cleaned_data.get("CambiarPassword")
        nueva = cleaned_data.get("Password")
        confirmar = cleaned_data.get("ConfirmarPassword")

        patron = r'^(?=.*[A-Za-z])(?=.*\d).{5,}$'

        if cambiar:
            if not nueva or not confirmar:
                raise forms.ValidationError("Debe ingresar y confirmar la contraseña.")

            if nueva != confirmar:
                raise forms.ValidationError("Las contraseñas no coinciden.")

            if not re.match(patron, nueva):
                raise forms.ValidationError(
                    "Debe contener mínimo 5 caracteres, 1 letra y 1 número."
                )

        return cleaned_data


    # =============================================================================
    # MÉTODO SAVE DEL UPDATE
    # =============================================================================
    # Este save aplica el cambio de contraseña solo si el usuario marcó la opción
    # "CambiarPassword". Si no, guarda solo los demás datos.
    # =============================================================================
    def save(self, commit=True):

        user = super().save(commit=False)

        cambiar = self.cleaned_data.get("CambiarPassword")
        nueva = self.cleaned_data.get("Password")

        if cambiar and nueva:
            user.Password = make_password(nueva)

        if commit:
            user.save()

        return user


    # =============================================================================
    # VALIDACIÓN DEL CAMPO Cargo
    # =============================================================================
    def clean_Cargo(self):
        cargo = self.cleaned_data.get('Cargo')

        if not Cargos.objects.exists():
            raise forms.ValidationError("Debe registrar cargos primero.")

        if cargo is None:
            raise forms.ValidationError("Debe seleccionar un cargo válido.")

        return cargo



    # =============================================================================
    # CONFIGURACIÓN DINÁMICA DE CAMPOS (__init__) EN FORMULARIO DE ACTUALIZACIÓN
    # =============================================================================
    # Aquí se aplican dos cosas:
    #
    #   1) Se deshabilita 'Empleado' → NO se permite cambiar el empleado asignado.
    #
    #   2) Se configura el select 'Cargo' igual que en el registro:
    #       - queryset
    #       - label_from_instance
    #       - empty_label
    #
    # Se mantiene *args y **kwargs para compatibilidad con Django.
    # =============================================================================
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)

        # Bloquear campo Empleado (no editable)
        self.fields['Empleado'].disabled = True
        

        self.fields['Cargo'].queryset = Cargos.objects.all()

        self.fields['Cargo'].label_from_instance = (
            lambda obj: f"{obj.TipoDeCargo} - {obj.DescripcionDelCargo}"
        )

        self.fields['Cargo'].empty_label = "Seleccione un cargo existente."
    

        
