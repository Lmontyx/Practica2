from django.urls import path  # Importa la función 'path' para definir las URL
from .views import (
    inicio, reg, exit, persona, 
    modificar_persona, eliminar_persona, 
    generar_pdf, seleccionar_persona, registrar_pago, buscar_pagos, eliminar_pago
)  # Importa las vistas que manejarán las solicitudes para estas URLs

urlpatterns = [
    path('', inicio, name='home'),  # Ruta para la página de inicio del sitio. Usa la vista 'inicio' y la etiqueta 'home'
    path('inicio/', inicio, name='inicio'),  # Ruta alternativa para la página de inicio. Usa la vista 'inicio' y la etiqueta 'inicio'
    path('reg/', reg, name='reg'),  # Ruta para el registro de usuarios. Usa la vista 'reg' y la etiqueta 'reg'
    path('logout/', exit, name='exit'),  # Ruta para el cierre de sesión. Usa la vista 'exit' y la etiqueta 'exit'
    path('persona/', persona, name='persona'),  # Ruta para la gestión de personas. Usa la vista 'persona' y la etiqueta 'persona'
    path('persona/modificar/<int:persona_id>/', modificar_persona, name='modificar_persona'),  # Ruta para modificar una persona específica. Usa la vista 'modificar_persona', requiere un ID de persona como parámetro
    path('persona/eliminar/<int:persona_id>/', eliminar_persona, name='eliminar_persona'),  # Ruta para eliminar una persona específica. Usa la vista 'eliminar_persona', requiere un ID de persona como parámetro
    path('generar_pdf/<int:pago_id>/', generar_pdf, name='generar_pdf'),  # Ruta para generar un PDF con información de pago específica. Usa la vista 'generar_pdf', requiere un ID de pago como parámetro
    path('registrar_pago/<int:persona_id>/', registrar_pago, name='registrar_pago'),  # Ruta para registrar un nuevo pago para una persona específica. Usa la vista 'registrar_pago', requiere un ID de persona como parámetro
    path('seleccionar_persona/', seleccionar_persona, name='seleccionar_persona'),  # Ruta para seleccionar una persona de una lista. Usa la vista 'seleccionar_persona' y la etiqueta 'seleccionar_persona'
    path('buscar_pagos/', buscar_pagos, name='buscar_pagos'),  # Ruta para buscar pagos. Usa la vista 'buscar_pagos' y la etiqueta 'buscar_pagos'
    path('eliminar_pago/<int:id>/', eliminar_pago, name='eliminar_pago'),  # Ruta para eliminar un pago específico. Usa la vista 'eliminar_pago', requiere un ID de pago como parámetro
]
