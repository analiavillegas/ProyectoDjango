from django.shortcuts import render, redirect
from .forms import ContactForm


def contacto(request):
    success = False
    form_data = {}
    errors = None

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            success = True
            form_data = form.cleaned_data
        else:
            errors = form.errors  # Captura los errores del formulario
    else:
        form = ContactForm()

    return render(request, 'usuarios/contacto.html', {
        'form': form,
        'success': success,
        'form_data': form_data,
        'errors': errors
    })

def saludo(request):
    contexto = {"nombre": "Juan"}
    return render(request, "usuarios/saludo.html", contexto)

def pagina_inicio(request):
    return render(request, 'usuarios/index.html')

from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json

@require_POST
def enviar_nombre(request):
    data = json.loads(request.body)
    nombre = data.get('nombre', 'Anónimo')
    mensaje = f"¡Hola, {nombre}!"
    return JsonResponse({'mensaje': mensaje})



def saludo(request):
    contexto = {
        'nombre': 'Juan',
        'color': 'Verde',
        'productos': ['Celular', 'Tablet', 'Laptop'],
        'precio': 1234.5678,
    }
    return render(request, 'usuarios/saludo.html', contexto)