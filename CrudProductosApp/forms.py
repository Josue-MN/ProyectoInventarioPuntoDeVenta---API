# Importaciones necesarias
from django import forms  # Importa el módulo de formularios de Django
from CrudProductosApp.models import Productos  # Importa el modelo Producto
import re
from datetime import date
from CrudCategoriaProductoApp.models import CategoriaProducto #Se importa el models para hacer uso de la llave foranea
from CrudBodegasApp.models import Bodegas

# ========================================================================
# Formulario: Registro de Productos
# ========================================================================
# Este formulario permite crear o actualizar registros de productos
# usando el modelo Producto. Al heredar de ModelForm, genera automáticamente
# campos basados en el modelo.
# ========================================================================

# Formulario para registrar productos basado en el modelo Productos
class ProductoRegistrationForm(forms.ModelForm):

    class Meta:
        model = Productos  # Modelo al que está vinculado el formulario
        fields = '__all__'  # Incluye todos los campos del modelo

        # Etiquetas visibles en el formulario
        labels = {
            'CodigoDeBarras': 'Codigo de barras',
            'ValorProducto': 'Valor',
            'StockProducto': 'Stock',
            'NombreProducto': 'Nombre del producto',
            'MarcaProducto': 'Marca del producto',
            'FechaDeVencimiento': 'Fecha de vencimiento',
            'CategoriaProducto': 'Categoria del Producto',
            'Bodegas': 'Asociar Bodega'
        }

        # Ayudas que aparecen junto a los campos
        help_texts = {
            'CodigoDeBarras': 'Indique el codigo de barras del producto a registrar',
            'ValorProducto': 'El valor aceptado es a partir de $1000',
            'StockProducto': 'No esta permitido registrar el producto sin stock',
            'NombreProducto': 'Ingrese el nombre tal cual muestra el producto',
            'MarcaProducto': 'Indique la marca la cual pertenece el producto',
            'FechaDeVencimiento': 'Indique la fecha de vencimiento mencionada en el producto (DD-MM-YYYY).',
            'CategoriaProducto': 'Indique la categoria a la que pertenece el producto',
            'Bodegas': 'Indique la bodega a la cual se asociara el producto'
        }

        # Mensajes de error personalizados
        error_messages = {
            'CodigoDeBarras': {
                'required': 'Por favor introduzca el codigo de barras',
                'unique': 'Este codigo de barras ya esta registrado',
                'invalid': 'Ingrese solamente numeros y sin espacios',
            },
            'ValorProducto': {
                'required': 'Por favor introduzca el valor del producto',
                'invalid': 'Ingrese un valor valido',
            },
            'StockProducto': {
                'required': 'Por favor introduzca el stock del producto',
                'invalid': 'Ingrese un stock valido',
            },
            'NombreProducto': {
                'required': 'Por favor introduzca el nombre del producto',
            },
            'MarcaProducto': {
                'required': 'Por favor introduzca la marca del producto',
            },
            'FechaDeVencimiento': {
                'required': 'Por favor introduzca la fecha de vencimiento del producto',
                'invalid': 'Ingrese una fecha válida en formato DD-MM-YYYY.'
            },
            'CategoriaProducto': {
                'required': 'Por favor introduzca la categoria del producto',
            },
            'Bodegas': {
                'required': 'Por favor introduzca la bodega a la que se asociara el producto',
            },
        }

        # Widgets para personalizar el HTML de cada campo
        widgets = {
            'CodigoDeBarras': forms.TextInput(attrs={'placeholder': 'Ej: 7802900000328'}),
            'ValorProducto': forms.NumberInput(attrs={'placeholder': 'Ej: $1500'}),
            'StockProducto': forms.NumberInput(attrs={'placeholder': 'Ej: 5 (unidades)'}),
            'NombreProducto': forms.TextInput(attrs={'placeholder': 'Ej: Papas fritas'}),
            'MarcaProducto': forms.TextInput(attrs={'placeholder': 'Ej: Fruna'}),
            'FechaDeVencimiento': forms.DateInput(format='%Y-%m-%d', attrs={'placeholder': 'DD-MM-YYYY', 'type': 'date'}),
        }

    # ====================================================================
    # Validaciones personalizadas por campo
    # ====================================================================

    # Valida que el código de barras sea solo números y único
    def clean_CodigoDeBarras(self):
        inputCodigoDeBarras = self.cleaned_data['CodigoDeBarras']
        expresion = r'^[0-9]+$'
        query = Productos.objects.filter(CodigoDeBarras=inputCodigoDeBarras)

        if not re.match(expresion, inputCodigoDeBarras):
            raise forms.ValidationError("Ingrese solamente numeros y sin espacios")
        if self.instance.pk:
            query = query.exclude(pk=self.instance.pk)  # Excluye el registro actual si es edición
        if query.exists():
            raise forms.ValidationError("Este Codigo de Barras ya está registrado.")
        return inputCodigoDeBarras

    # Valida que el valor del producto sea positivo y mínimo 3 dígitos
    def clean_ValorProducto(self):
        inputValorProducto = self.cleaned_data['ValorProducto']

        if inputValorProducto < 0:
            raise forms.ValidationError("No puede ingresar valores negativos")
        if len(str(inputValorProducto)) < 3:
            raise forms.ValidationError("Debe ingresar un valor valido a partir de 3 digitos ($123)")
        if inputValorProducto == 0:
            raise forms.ValidationError("El valor no puede ser 0")
        return inputValorProducto

    # Valida que el stock sea positivo y mayor a 0
    def clean_StockProducto(self):
        inputStockProducto = self.cleaned_data['StockProducto']

        if inputStockProducto < 0:
            raise forms.ValidationError("No puede ingresar stock negativos")
        if inputStockProducto == 0:
            raise forms.ValidationError("El Stock no puede ser 0")
        return inputStockProducto

    # Valida que el nombre del producto no contenga caracteres especiales y tenga formato correcto
    def clean_NombreProducto(self):
        inputNombreProducto = self.cleaned_data['NombreProducto'].strip()
        caracteres = r'^[A-Za-zÁÉÍÓÚÑáéíóúñ]+(?: [A-Za-zÁÉÍÓÚÑáéíóúñ]+)*(?: \d+[gG]?)?$'

        if not re.match(caracteres, inputNombreProducto):
            raise forms.ValidationError(
                "Ingrese un nombre del producto sin caracteres especiales, con de mas de 5 letras, "
                "sin juntar numeros ni letras y no con mas de 1 espacio entre caracteres."
            )
        return inputNombreProducto

    # Valida que la fecha de vencimiento sea posterior a la fecha actual
    def clean_FechaDeVencimiento(self):
        inputFechaDeVencimiento = self.cleaned_data['FechaDeVencimiento']

        if not inputFechaDeVencimiento:
            raise forms.ValidationError("Debe ingresar una fecha de vencimiento.")
        
        fecha_actual = date.today()
        if inputFechaDeVencimiento < fecha_actual:
            raise forms.ValidationError("La fecha de vencimiento no puede ser anterior a la fecha actual.")

        return inputFechaDeVencimiento

    ###VALIDACION FOREIGN KEY CATEGORIA
    def clean_CategoriaProducto(self):
        # Obtiene la categoría seleccionada
        ExisteCategoriaProducto = self.cleaned_data.get('CategoriaProducto')
        # Si no existen categorías registradas en la BD
        if not CategoriaProducto.objects.exists():
            raise forms.ValidationError("Debes registrar al menos una categoría para poder seleccionar una.")
        # Si el usuario no seleccionó ninguna categoría
        if ExisteCategoriaProducto is None:
            raise forms.ValidationError("Debes seleccionar una categoría de producto.")
        # Retorna la categoría válida
        return ExisteCategoriaProducto

    ###VALIDACION FOREIGN KEY BODEGA
    def clean_Bodegas(self):
        # Obtiene la categoría seleccionada
        ExisteBodegas = self.cleaned_data.get('Bodegas')
        # Si no existen bodegas registradas en la BD
        if not Bodegas.objects.exists():
            raise forms.ValidationError("Debes registrar al menos una bodega para poder seleccionar una.")
        # Si el usuario no seleccionó ninguna bodega
        if ExisteBodegas is None:
            raise forms.ValidationError("Debes seleccionar una bodega para el producto.")
        # Retorna la categoría válida
        return ExisteBodegas
    

    def __init__(self, *args, **kwargs):
        # Llama al constructor original del formulario
        super().__init__(*args, **kwargs)

        # Fuerza el formato de fecha (AAAA-MM-DD) para el campo FechaDeVencimiento
        self.fields['FechaDeVencimiento'].input_formats = ['%Y-%m-%d']
        
        # Configura el campo de categoría para que muestre todas las categorías disponibles
        self.fields['CategoriaProducto'].queryset = CategoriaProducto.objects.all()
         # Define cómo se mostrará cada categoría en el desplegable (usa su nombre)
        self.fields['CategoriaProducto'].label_from_instance = lambda obj: obj.NombreCategoria
         # Establece una etiqueta por defecto cuando no se ha seleccionado una categoría
        self.fields['CategoriaProducto'].empty_label = "Seleccione una categoria existente."


        # Configura el campo de categoría para que muestre todas las categorías disponibles
        self.fields['Bodegas'].queryset = Bodegas.objects.all()
         # Define cómo se mostrará cada categoría en el desplegable (usa su nombre)
        self.fields['Bodegas'].label_from_instance = lambda obj: obj.NombreBodega
         # Establece una etiqueta por defecto cuando no se ha seleccionado una categoría
        self.fields['Bodegas'].empty_label = "Seleccione una bodega existente."
