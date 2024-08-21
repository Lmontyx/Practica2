from django import forms  # Importa el módulo forms de Django para crear formularios
from django.contrib.auth.forms import UserCreationForm  # Importa UserCreationForm para manejar la creación de usuarios
from django.contrib.auth.models import User  # Importa el modelo User para gestionar los usuarios
from .models import Persona  # Importa el modelo Persona definido en models.py

# Define un formulario personalizado para la creación de usuarios
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # Usa el modelo User de Django para la creación de usuarios
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')  # Campos incluidos en el formulario

    # Configura textos de ayuda para los campos del formulario
    help_texts = {
        'username': '150 carácteres como máximo. Únicamente letras, dígitos y @/./+/-/_',
    }

    # Configura mensajes de error personalizados para los campos del formulario
    error_messages = {
        'username': {
            'max_length': 'Nombre de usuario muy largo.',
            'unique': 'El nombre de usuario ya está en uso.',
        },
        'password2': {
            'password_mismatch': 'Las contraseñas no coinciden.',
        },
    }

    # Inicializa el formulario y configura el texto de ayuda para el campo de la contraseña
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = "Su contraseña debe contener al menos 8 caracteres. No puede ser una clave utilizada comúnmente ni completamente numérica."

# Define un formulario basado en el modelo Persona
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona  # Usa el modelo Persona definido en models.py
        fields = ['nombre', 'apellido', 'direccion', 'localidad', 'telefono']  # Campos incluidos en el formulario

# Define un formulario para gestionar pagos
class PagoForm(forms.Form):
    monto = forms.DecimalField(max_digits=10, decimal_places=2)  # Campo para ingresar el monto del pago, con hasta 10 dígitos en total y 2 decimales
