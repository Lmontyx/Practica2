from django.contrib import admin  # Importa el módulo de administración de Django
from django.urls import path, include  # Importa las funciones path e include para definir rutas de URL

urlpatterns = [
    path('', include('myapp.urls')),  # Incluye las URL definidas en el archivo urls.py de la aplicación 'myapp'
    path('admin/', admin.site.urls),  # Define la URL para acceder al panel de administración de Django
    path('accounts/', include('django.contrib.auth.urls')),  # Incluye las URLs de autenticación proporcionadas por Django para gestionar el inicio de sesión, cierre de sesión, cambio de contraseña, etc.
]
