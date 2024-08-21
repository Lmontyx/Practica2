from django.shortcuts import render, redirect, get_object_or_404  # Importa funciones para renderizar plantillas, redirigir y obtener objetos
from django.contrib.auth.decorators import login_required  # Importa el decorador para requerir autenticación
from django.contrib.auth import logout  # Importa la función para cerrar sesión
from django.contrib import messages  # Importa el módulo para manejar mensajes
from django.http import HttpResponse  # Importa HttpResponse para devolver respuestas HTTP
from .forms import CustomUserCreationForm, PersonaForm, PagoForm  # Importa formularios personalizados
from .models import Persona, Pago  # Importa los modelos Persona y Pago
from django.template.loader import render_to_string  # Importa la función para renderizar plantillas a cadenas de texto
import pdfkit  # Importa pdfkit para generar PDFs
from django.core.paginator import Paginator  # Importa el paginador para dividir los resultados en páginas

# Configura pdfkit para encontrar wkhtmltopdf
config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')  # Especifica la ruta del ejecutable wkhtmltopdf

@login_required
def inicio(request):
    personas = Persona.objects.all()  # Obtiene todos los objetos Persona
    return render(request, 'core/inicio.html', {'personas': personas})  # Renderiza la plantilla 'inicio.html' con el contexto de las personas

@login_required
def home(request):
    return render(request, 'core/home.html')  # Renderiza la plantilla 'home.html'

@login_required
def reg(request):
    data = {
        'form': CustomUserCreationForm()  # Crea un formulario de registro de usuario vacío
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)  # Crea un formulario con los datos del POST
        if user_creation_form.is_valid():
            user_creation_form.save()  # Guarda el nuevo usuario
            messages.success(request, 'Usuario registrado exitosamente.')  # Muestra un mensaje de éxito
        else:
            messages.error(request, 'Hubo un error en el registro. Por favor, inténtalo de nuevo.')  # Muestra un mensaje de error
            data['form'] = user_creation_form  # Añade el formulario con errores al contexto

    return render(request, 'core/reg.html', data)  # Renderiza la plantilla 'reg.html' con el contexto del formulario

@login_required
def exit(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('home')  # Redirige a la página de inicio

@login_required
def persona(request):
    search_query = request.GET.get('search', '')  # Obtiene el término de búsqueda del GET
    personas_list = Persona.objects.filter(
        nombre__icontains=search_query
    ) | Persona.objects.filter(
        apellido__icontains=search_query
    )  # Filtra personas por nombre o apellido que contengan el término de búsqueda
    
    paginator = Paginator(personas_list, 5)  # Configura el paginador para mostrar 5 personas por página
    page_number = request.GET.get('page')  # Obtiene el número de página del GET
    personas = paginator.get_page(page_number)  # Obtiene la página actual de personas
    
    if request.method == 'POST':
        form = PersonaForm(request.POST)  # Crea un formulario con los datos del POST
        if form.is_valid():
            form.save()  # Guarda la nueva persona
            messages.success(request, 'Persona registrada exitosamente.')  # Muestra un mensaje de éxito
            return redirect('persona')  # Redirige a la página de gestión de personas
    else:
        form = PersonaForm()  # Crea un formulario vacío

    return render(request, 'core/personas.html', {'form': form, 'personas': personas})  # Renderiza la plantilla 'personas.html' con el contexto del formulario y las personas paginadas

@login_required
def modificar_persona(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)  # Obtiene la persona o retorna 404 si no se encuentra
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)  # Crea un formulario con los datos del POST y la instancia de persona
        if form.is_valid():
            form.save()  # Guarda los cambios en la persona
            messages.success(request, 'Persona modificada exitosamente.')  # Muestra un mensaje de éxito
            return redirect('persona')  # Redirige a la página de gestión de personas
    else:
        form = PersonaForm(instance=persona)  # Crea un formulario con la instancia de persona para editar

    return render(request, 'core/modificar_persona.html', {'form': form})  # Renderiza la plantilla 'modificar_persona.html' con el contexto del formulario

@login_required
def eliminar_persona(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)  # Obtiene la persona o retorna 404 si no se encuentra
    if request.method == 'POST':
        persona.delete()  # Elimina la persona
        messages.success(request, 'Persona eliminada exitosamente.')  # Muestra un mensaje de éxito
        return redirect('persona')  # Redirige a la página de gestión de personas
    return render(request, 'core/eliminar_persona.html', {'persona': persona})  # Renderiza la plantilla 'eliminar_persona.html' con el contexto de la persona a eliminar

@login_required
def seleccionar_persona(request):
    search_query = request.GET.get('search', '')  # Obtiene el término de búsqueda del GET
    personas = Persona.objects.filter(
        nombre__icontains=search_query
    ) | Persona.objects.filter(
        apellido__icontains=search_query
    )  # Filtra personas por nombre o apellido que contengan el término de búsqueda
    
    # Limitar los resultados a los primeros 5
    personas = personas[:5]

    return render(request, 'core/seleccionar_persona.html', {'personas': personas})  # Renderiza la plantilla 'seleccionar_persona.html' con el contexto de las personas filtradas

@login_required
def generar_pdf(request, pago_id):
    pago = get_object_or_404(Pago, id=pago_id)  # Obtiene el pago o retorna 404 si no se encuentra
    context = {'pago': pago}  # Contexto para la plantilla del PDF

    # Renderiza la plantilla a un string HTML
    html_string = render_to_string('core/persona_pdf.html', context)

    # Generar PDF usando pdfkit
    pdf_output = pdfkit.from_string(html_string, False, configuration=config)

    # Configurar la respuesta HTTP
    response = HttpResponse(pdf_output, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="pago_{pago.id}.pdf"'  # Configura el nombre del archivo PDF para la descarga

    return response

@login_required
def registrar_pago(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)  # Obtiene la persona o retorna 404 si no se encuentra
    
    if request.method == 'POST':
        form = PagoForm(request.POST)  # Crea un formulario con los datos del POST
        if form.is_valid():
            monto = form.cleaned_data['monto']  # Obtiene el monto del formulario
            pago = Pago(persona=persona, monto=monto)  # Crea una nueva instancia de Pago
            pago.save()  # Guarda el nuevo pago
            
            # Generar PDF
            context = {'persona': persona, 'pago': pago}
            html_string = render_to_string('core/persona_pdf.html', context)
            
            # Generar PDF usando pdfkit
            pdf_output = pdfkit.from_string(html_string, False, configuration=config)

            # Configurar la respuesta HTTP
            response = HttpResponse(pdf_output, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="pago_{pago.id}.pdf"'  # Configura el nombre del archivo PDF para la descarga
            return response
    else:
        form = PagoForm()  # Crea un formulario vacío

    return render(request, 'core/registrar_pago.html', {'form': form, 'persona': persona})  # Renderiza la plantilla 'registrar_pago.html' con el contexto del formulario y la persona

@login_required
def buscar_pagos(request):
    search_query = request.GET.get('search', '')  # Obtiene el término de búsqueda del GET
    pagos = Pago.objects.filter(persona__nombre__icontains=search_query) | Pago.objects.filter(persona__apellido__icontains=search_query)
    return render(request, 'core/buscar_pagos.html', {'pagos': pagos})  # Renderiza la plantilla 'buscar_pagos.html' con el contexto de los pagos filtrados

def eliminar_pago(request, id):
    pago = get_object_or_404(Pago, id=id)  # Obtiene el pago o retorna 404 si no se encuentra
    if request.method == 'POST':
        pago.delete()  # Elimina el pago
        return redirect('buscar_pagos')  # Redirige a la página de búsqueda de pagos
    return redirect('buscar_pagos')  # Redirige a la página de búsqueda de pagos si el método no es POST
