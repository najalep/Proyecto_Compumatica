from django.forms import ModelForm
from .models import *
from django import forms
from datetime import datetime

class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['names'].widget.attrs['autofocus'] = True

    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'names': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombres',
                }
            ),
            'surnames': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'cedula': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su cedula',
                }
            ),
            'birthday': forms.DateInput(format=('%Y-%m-%d'),attrs={'type':'date' }),
            'address': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su dirección',
                }
            ),

        }



class AreaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['names'].widget.attrs['autofocus'] = True

    class Meta:
        model = Area
        fields = '__all__'
        widgets = {
            'names': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombres',
                }
            ),
        }


class EmpleadoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['names'].widget.attrs['autofocus'] = True

    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'names': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombres',
                }
            ),
            'surnames': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'cedula': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su cedula',
                }
            ),
            'birthday': forms.DateInput(format=('%Y-%m-%d'),attrs={'type':'date' }),
            'area': forms.Select(),

        }


class CategoriaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['names'].widget.attrs['autofocus'] = True

    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'names': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombre',
                }
            ),
        }


class MarcaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['names'].widget.attrs['autofocus'] = True

    class Meta:
        model = Marca
        fields = '__all__'
        widgets = {
            'names': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombre',
                }
            ),
        }


class ArticuloForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['code'].widget.attrs['autofocus'] = True

    class Meta:
        model = Articulo
        fields = '__all__'
        widgets = {
            'code': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su codigo',
                }
            ),

            'device': forms.Select(),

            'names': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su nombre',
                }
            ),

            'brand': forms.Select(),

            'pvp': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el Precio',
                }
            ),
        }



class FacturaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cli'].queryset = Client.objects.none()

        self.fields['iva'].widget.attrs = {
            'readonly': True,
            'class': 'form-control',
        }

        self.fields['subtotal'].widget.attrs ={
            'readonly': True,
            'class':'form-control',
        }

        self.fields['total'].widget.attrs = {
            'readonly': True,
            'class': 'form-control',
        }

    class Meta:
        model = Factura
        fields = '__all__'
        widgets = {
            'cli': forms.Select(attrs={
                'class': 'form-control',
                'style': 'width: 100%'
            }),
            'date_joined': forms.DateInput(format=('%Y-%m-%d'),attrs={'type':'date' })}






















