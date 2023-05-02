from django.urls import path
from AppFinal import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('usuarios', views.usuarios, name="Usuarios"),
    path('vehiculos', views.vehiculos, name="Vehiculos"),
    path('comentarios', views.comentarios, name="Comentarios"),
    path('buscarusuario/', views.buscarusuario),
    path('buscarvehiculo/', views.buscarvehiculo),
    path('administrador/', views.administrador_menu, name="Administrador"),
    path('administradorusuario/', views.leerUsuarios, name="admin_user"),
    path('administradorvehiculo/', views.leerVehiculos, name="admin_vehicle"),
    path('administradorcomentario/', views.leerComentarios, name="admin_coment"),
]