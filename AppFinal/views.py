from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppFinal.forms import UsuarioFormulario

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
    return render(request, "AppFinal/vehiculos.html")

def comentarios(request):
    return render(request, "AppFinal/comentarios.html")

