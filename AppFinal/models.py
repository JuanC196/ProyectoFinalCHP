from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre= models.CharField(max_length=40)
    email= models.EmailField()
    telefono = models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Email {self.email} - Telefono: {self.telefono}"

class Vehiculos(models.Model):
    marca= models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    modelo= models.IntegerField()
    precio= models.IntegerField()
    def __str__(self):
        return f"Marca: {self.marca} - Tipo: {self.tipo} - Modelo: {self.modelo} - Precio: {self.precio}"

class Comentario(models.Model):
    nombre= models.CharField(max_length=40)
    email = models.EmailField()
    telefono = models.IntegerField()
    texto= models.CharField(max_length=100)
    def __str__(self):
        return f"Nombre: {self.nombre} - Email: {self.email} - Telefono: {self.telefono} - Texto: {self.texto}"   

