from django.db import models

# Create your models here.
class Usuario(models.Model):

    nombre= models.CharField(max_length=40)
    email= models.EmailField()
    telefono = models.IntegerField()

class Vehiculos(models.Model):
    marca= models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    modelo= models.IntegerField()
    precio= models.IntegerField()

class Comentario(models.Model):
    nombre= models.CharField(max_length=40)
    email = models.EmailField()
    telefono = models.IntegerField()
    texto= models.CharField(max_length=100)   

