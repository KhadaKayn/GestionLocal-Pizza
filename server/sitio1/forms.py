from django import forms
from .models import TipoMasa, Tamanos, Ingredientes, Contacto, Pizza, CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Este campo es obligatorio.')
    direccion = forms.CharField(max_length=255, help_text='Dirección de domicilio.')
    telefono = forms.CharField(max_length=15, help_text='Número de teléfono de contacto.')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'direccion', 'telefono', 'password1', 'password2']

class IngredientesForm(forms.ModelForm):
    class Meta:
        model = Ingredientes
        fields = ['nombre', 'stock', 'precio', 'oferta', 'descuento', 'imagen']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Agregar un script de jQuery para mostrar u ocultar el campo de descuento
        self.fields['oferta'].widget.attrs['onclick'] = (
            '$("#id_descuento").toggle(this.checked);'
        )
        self.fields['oferta'].widget.attrs['checked'] = 'checked'

    def clean_descuento(self):
        descuento = self.cleaned_data.get('descuento')
        oferta = self.cleaned_data.get('oferta')

        if oferta and (descuento < 1 or descuento > 99):
            raise forms.ValidationError("El descuento debe estar entre 1% y 99%.")
        
        return descuento

class TipoMasaForm(forms.ModelForm):
    class Meta:
        model = TipoMasa
        fields = ['nombre', 'disponible', 'precio', 'oferta', 'descuento', 'imagen']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Agregar un script de jQuery para mostrar u ocultar el campo de descuento
        self.fields['oferta'].widget.attrs['onclick'] = (
            '$("#id_descuento").toggle(this.checked);'
        )
        self.fields['oferta'].widget.attrs['checked'] = 'checked'


    def clean_descuento(self):
        descuento = self.cleaned_data.get('descuento')
        oferta = self.cleaned_data.get('oferta')

        if oferta and (descuento < 1 or descuento > 99):
            raise forms.ValidationError("El descuento debe estar entre 1% y 99%.")
        
        return descuento
    

class TamanosForm(forms.ModelForm):
    class Meta:
        model = Tamanos
        fields = ['nombre', 'disponible', 'precio', 'oferta', 'descuento', 'imagen']
        error_messages = {
            'nombre': {
                'unique': "El tamaño ya existe. Por favor, ingrese un tamaño diferente.",
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Agregar un script de jQuery para mostrar u ocultar el campo de descuento
        self.fields['oferta'].widget.attrs['onclick'] = (
            '$("#id_descuento").toggle(this.checked);'
        )
        self.fields['oferta'].widget.attrs['checked'] = 'checked'

        
    def clean_descuento(self):
        descuento = self.cleaned_data.get('descuento')
        oferta = self.cleaned_data.get('oferta')

        if oferta and (descuento < 1 or descuento > 99):
            raise forms.ValidationError("El descuento debe estar entre 1% y 99%.")
        
        return descuento
    
class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['nombre', 'descripcion', 'tamano', 'tipo_masa', 'imagen', 'ingredientes']

    ingredientes = forms.ModelMultipleChoiceField(
        queryset=Ingredientes.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True  # False Para permitir pizzas sin ingredientes
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Modificar el queryset para incluir solo tamaños disponibles
        self.fields['tamano'].queryset = Tamanos.objects.filter(disponible=True)

        # Modificar el queryset para incluir solo tipos de masa disponibles
        self.fields['tipo_masa'].queryset = TipoMasa.objects.filter(disponible=True)

        # Modificar el queryset para incluir solo ingredientes en stock
        self.fields['ingredientes'].queryset = Ingredientes.objects.filter(stock__gt=0)

    def save(self, commit=True):
        pizza = super().save(commit=False)
        pizza.precio = pizza.calcular_precio()

        if commit:
            pizza.save()

            # Actualizar los ingredientes asociados a la pizza
            pizza.ingredientes.set(self.cleaned_data['ingredientes'])
            pizza.save()

        return pizza

    