from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppFinal.forms import *

# Create your views here.
def inicio(request):
    return render(request, "AppFinal/inicio.html")

def usuarios(request):
    if request.method == 'POST':
       miFormulario = UsuarioFormulario(request.POST) 
       print(miFormulario)

       if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            usuario = Usuario(nombre=informacion['nombre'],email=informacion['email'],telefono=informacion['telefono'])

            usuario.save()
        
            return render(request, "AppFinal/inicio.html")
    else:
       miFormulario = UsuarioFormulario()
    
    return render(request, "AppFinal/usuarios.html", {"miFormulario": miFormulario})

def vehiculos(request):
    if request.method == 'POST':
       miFormulario = VehiculoFormulario(request.POST) 
       print(miFormulario)

       if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            vehiculo = Vehiculos(marca=informacion['marca'],tipo=informacion['tipo'],modelo=informacion['modelo'],precio=informacion['precio'] )

            vehiculo.save()
        
            return render(request, "AppFinal/inicio.html")
    else:
       miFormulario = VehiculoFormulario()
    
    return render(request, "AppFinal/vehiculos.html", {"miFormulario": miFormulario})

def comentarios(request):
    if request.method == 'POST':
       miFormulario = ComentarioFormulario(request.POST) 
       print(miFormulario)

       if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            comentario = Comentario(nombre=informacion['nombre'],email=informacion['email'],telefono=informacion['telefono'],texto=informacion['texto'])

            comentario.save()
        
            return render(request, "AppFinal/inicio.html")
    else:
       miFormulario = ComentarioFormulario()
    
    return render(request, "AppFinal/comentarios.html", {"miFormulario": miFormulario})

def buscar(request):
    
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        usuarios = Usuario.objects.filter(nombre__icontains=nombre)
    
        return render(request, "AppFinal/usuarios.html", {"usuarios":usuarios,"nombre":nombre})
    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)