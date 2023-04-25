from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, "AppFinal/inicio.html")

def usuarios(request):
    return render(request, "AppFinal/usuarios.html")

def vehiculos(request):
    return render(request, "AppFinal/vehiculos.html")

def comentarios(request):
    return render(request, "AppFinal/comentarios.html")