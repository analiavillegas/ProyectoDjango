from django.shortcuts import render, get_object_or_404, redirect
from .forms import ConsultasForm
from django.http import JsonResponse
from django.core.mail import send_mail
from .models import Consultas

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required











def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # inicia sesión automáticamente tras registrarse
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'mi_app/registro.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'mi_app/dashboard.html')






# Eliminar consulta
def eliminar_consulta(request, consulta_id):
    consulta = get_object_or_404(Consultas, id=consulta_id)
    consulta.delete()
    return JsonResponse({"success": True, "message": "Consulta eliminada correctamente"})

# Modificar consulta
def modificar_consulta(request, consulta_id):
    consulta = get_object_or_404(Consultas, id=consulta_id)  # Obtener la consulta

    if request.method == 'POST':
        form = ConsultasForm(request.POST)
        if form.is_valid():

            # Actualizar los valores de la consulta
            consulta.nombre = form.cleaned_data["nombre"]
            consulta.email = form.cleaned_data["email"]
            consulta.mensaje = form.cleaned_data["mensaje"]
            consulta.save()  # Guardar cambios en la base de datos

            return redirect('listado_consultas')  # Redirigir al listado

    else:
        # Llenar el formulario con los datos actuales de la consulta
        form = ConsultasForm(initial={
           'nombre': consulta.nombre,
           'email': consulta.email,
           'mensaje': consulta.mensaje
        })

    return render(request, 'mi_app/modificar_consulta.html', {'form': form})





# Listado de consultas
def listado_consultas(request):
    consultas = Consultas.objects.all()  # Obtener todas las consultas
    return render(request, 'mi_app/listado_consultas.html', {'consultas': consultas})



def consultas(request):
    if request.method == 'POST':
        form = ConsultasForm(request.POST)
        # Verificar si el formulario es válido
        if form.is_valid():

            # Obtener datos del formulario
            nombre = form.cleaned_data["nombre"]
            email = form.cleaned_data["email"]
            mensaje = form.cleaned_data["mensaje"]

            # Guardar en la base de datos
            consulta = Consultas(nombre=nombre, email=email, mensaje=mensaje)
            consulta.save()

            # Construir mensaje a enviar
            asunto = f"Consulta de {nombre}"
            cuerpo_mensaje = f"Nombre: {nombre}\nCorreo: {email}\n\nMensaje:\n{mensaje}"
            destinatario = "destinatario@gmail.com" # Solo funcionará si se utiliza Servidor SMTP real

            try:
                # Enviar correo
                send_mail(asunto, cuerpo_mensaje, email, [destinatario], fail_silently=False)

                # Devolver respuesta si el correo se envió correctamente
                return JsonResponse({"success": True, "message": "¡Consulta enviada correctamente!"})

            except Exception as e:
                # Devolver respuesta si el envío falló
                return JsonResponse({"success": False, "message": f"Error al enviar el email: {str(e)}"})

        # Devolver respuesta si el formulario no es válido (errores detectados)
        else:
            return JsonResponse({"success": False, "errors": form.errors})
    else:
        form = ConsultasForm()

    return render(request, 'mi_app/consultas.html', {'form': form})


def pagina_inicio(request):
    return render(request,'mi_app/index.html')




def formulario_view(request):
    resultado = ""

    if request.method == "POST":
        nombre = request.POST.get('nombre')
        edad = int(request.POST.get('edad', 0))

        if edad >= 18:
            resultado = f"{nombre}, calificás para el crédito."
        else:
            resultado = f"{nombre}, no calificás por ser menor de edad."

    return render(request, 'mi_app/formulario.html', {'resultado': resultado})


