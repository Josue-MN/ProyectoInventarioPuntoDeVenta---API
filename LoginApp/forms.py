# Importación del módulo de formularios de Django
from django import forms

# Este formulario se utiliza para capturar el username y
# password del usuario al momento de iniciar sesión.
# NO está vinculado a ningún modelo (ModelForm), por lo
# que simplemente valida datos ingresados manualmente.
# ---------------------------------------------------------
class LoginForm(forms.Form):

    # Campo de texto para ingresar el nombre de usuario.
    # Se usa CharField porque es texto simple.
    UsernameField = forms.CharField(
        label="Ingresa tu username"   # Texto visible junto al input
    )

    # Campo de texto para contraseña.
    PasswordField = forms.CharField(
        label="Ingresa tu password",
        widget=forms.PasswordInput(render_value=False)
    )

    # Meta define qué campos se incluirán en el formulario.
    class Meta:
        fields = ['UsernameField', 'PasswordField']
