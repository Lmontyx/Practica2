import os
from pathlib import Path

# Definición de BASE_DIR como el directorio base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta utilizada para proporcionar seguridad criptográfica. 
# Debe mantenerse en secreto en entornos de producción.
SECRET_KEY = 'django-insecure-2%wjw%p6e7#s9ynxjz!c^_afk%$(^%%155$ygy$nebdy2&-9$$'

# Modo de depuración activado para desarrollo. 
# Debe estar en False en producción para evitar la exposición de detalles del sistema.
DEBUG = True

# Lista de direcciones IP o dominios permitidos para acceder al proyecto. 
# Debe configurarse en producción.
ALLOWED_HOSTS = []


# Definición de aplicaciones instaladas en el proyecto
INSTALLED_APPS = [
    'django.contrib.admin',  # Interfaz administrativa de Django
    'django.contrib.auth',  # Sistema de autenticación de usuarios
    'django.contrib.contenttypes',  # Sistema de tipos de contenido
    'django.contrib.sessions',  # Manejo de sesiones
    'django.contrib.messages',  # Sistema de mensajes
    'django.contrib.staticfiles',  # Manejo de archivos estáticos
    'crispy_forms',  # Paquete para mejorar la presentación de formularios
    'crispy_bootstrap5',  # Paquete para usar Bootstrap 5 con crispy_forms
    'myapp',  # Tu aplicación personalizada
]

# Configuración del almacenamiento de mensajes y mapeo de niveles de mensaje a clases CSS
from django.contrib.messages import constants as messages
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

# Configuración para crispy_forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Middleware para manejar diferentes aspectos de las solicitudes y respuestas
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Seguridad de la aplicación
    'django.contrib.sessions.middleware.SessionMiddleware',  # Manejo de sesiones
    'django.middleware.common.CommonMiddleware',  # Funciones comunes para solicitudes
    'django.middleware.csrf.CsrfViewMiddleware',  # Protección contra ataques CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Autenticación de usuarios
    'django.contrib.messages.middleware.MessageMiddleware',  # Manejo de mensajes
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Protección contra clickjacking
]

# Archivo de URL principal del proyecto que define cómo se enrutan las solicitudes
ROOT_URLCONF = 'PP2.urls'

# Configuración del sistema de plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Backend de plantillas de Django
        'DIRS': [],  # Directorios adicionales para buscar plantillas
        'APP_DIRS': True,  # Habilita la búsqueda de plantillas en directorios de aplicaciones
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Procesador de contexto de depuración
                'django.template.context_processors.request',  # Procesador de contexto de solicitud
                'django.contrib.auth.context_processors.auth',  # Procesador de contexto de autenticación
                'django.contrib.messages.context_processors.messages',  # Procesador de contexto de mensajes
            ],
        },
    },
]

# Configuración de la aplicación WSGI para el despliegue del proyecto
WSGI_APPLICATION = 'PP2.wsgi.application'


# Configuración de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Motor de base de datos SQLite3
        'NAME': BASE_DIR / 'db.sqlite3',  # Ruta al archivo de base de datos
    }
}

# Validadores de contraseñas para asegurar contraseñas seguras
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Valida la similitud con atributos de usuario
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Valida la longitud mínima de la contraseña
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Valida que la contraseña no sea común
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Valida que la contraseña tenga números
    },
]


# Configuración de internacionalización y zona horaria
LANGUAGE_CODE = 'es'  # Idioma predeterminado del proyecto

TIME_ZONE = 'UTC'  # Zona horaria del proyecto

USE_I18N = True  # Habilita la internacionalización para traducción de contenido
USE_TZ = True  # Habilita el uso de zonas horarias

# Configuración para archivos estáticos (CSS, JavaScript, Imágenes)
STATIC_URL = '/static/'  # URL para servir archivos estáticos

# Tipo de campo predeterminado para claves primarias auto-generadas en los modelos
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Variables de redirección después de inicio y cierre de sesión
LOGIN_REDIRECT_URL = 'inicio'  # URL a redirigir después de iniciar sesión
LOGOUT_REDIRECT_URL = 'inicio'  # URL a redirigir después de cerrar sesión
