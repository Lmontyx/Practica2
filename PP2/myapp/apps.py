from django.apps import AppConfig  # Importa la clase AppConfig de Django para configurar una aplicación

class MyappConfig(AppConfig):  # Define una clase de configuración para la aplicación 'myapp'
    default_auto_field = 'django.db.models.BigAutoField'  # Establece el tipo de campo predeterminado para claves primarias auto-generadas en esta aplicación
    name = 'myapp'  # Define el nombre de la aplicación, que debe coincidir con el nombre del directorio de la aplicación
