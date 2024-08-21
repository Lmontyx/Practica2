from django.db import models  # Importa el módulo de modelos de Django para definir modelos de base de datos
from django.utils import timezone  # Importa el módulo timezone para manejar fechas y horas

# Define el modelo Persona para almacenar información de personas
class Persona(models.Model):
    nombre = models.CharField(max_length=100)  # Campo de texto para el nombre de la persona, con un máximo de 100 caracteres
    apellido = models.CharField(max_length=100)  # Campo de texto para el apellido de la persona, con un máximo de 100 caracteres
    direccion = models.CharField(max_length=255)  # Campo de texto para la dirección de la persona, con un máximo de 255 caracteres
    localidad = models.CharField(max_length=100)  # Campo de texto para la localidad de la persona, con un máximo de 100 caracteres
    telefono = models.CharField(max_length=15)  # Campo de texto para el teléfono de la persona, con un máximo de 15 caracteres
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Campo decimal para el monto pagado, con hasta 10 dígitos en total y 2 decimales
    fecha_pago = models.DateField(null=True, blank=True)  # Campo de fecha para la fecha del pago, puede ser nulo o estar en blanco

    def __str__(self):
        return f"{self.nombre} {self.apellido}"  # Representación en cadena del objeto Persona, devuelve el nombre y apellido

# Define el modelo Pago para registrar los pagos realizados por personas
class Pago(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)  # Relación de clave externa con el modelo Persona, eliminando los pagos asociados si se elimina la persona
    monto = models.DecimalField(max_digits=10, decimal_places=2)  # Campo decimal para el monto del pago, con hasta 10 dígitos en total y 2 decimales
    fecha = models.DateField(auto_now_add=True)  # Campo de fecha que se establece automáticamente con la fecha actual cuando se crea un nuevo pago
