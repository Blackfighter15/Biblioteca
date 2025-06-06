from django import forms
from .models import Usuario, Libro, Prestamo,Autor
from django.forms.widgets import TextInput

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        exclude = ['disponible']

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(PrestamoForm, self).__init__(*args, **kwargs)
        self.fields['libro'].queryset = Libro.objects.filter(disponible=True)

        self.fields['fecha_devolucion'].widget = forms.DateInput(attrs={'type': 'date', 'class': 'ui input'})

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'