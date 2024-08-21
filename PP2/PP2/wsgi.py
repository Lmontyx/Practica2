import os  # Importa el módulo os para interactuar con el sistema operativo

from django.core.wsgi import get_wsgi_application  # Importa la función get_wsgi_application de Django para configurar WSGI

# Establece la variable de entorno DJANGO_SETTINGS_MODULE para indicar el archivo de configuración de settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PP2.settings')

# Obtiene la aplicación WSGI para el proyecto Django, que sirve como punto de entrada para servidores WSGI
application = get_wsgi_application()
