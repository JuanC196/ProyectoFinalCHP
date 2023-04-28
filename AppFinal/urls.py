from django.urls import path
from AppFinal import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('usuarios', views.usuarios, name="Usuarios"),
    path('vehiculos', views.vehiculos, name="Vehiculos"),
    path('comentarios', views.comentarios, name="Comentarios"),
    path('buscarusuario/', views.buscarusuario),
    path('buscarvehiculo/', views.buscarvehiculo),
]