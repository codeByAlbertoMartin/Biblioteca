# Modelo para Autores
from django.db import models
from django.contrib.auth.models import User


class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=100)
    biografia = models.TextField()
    email = models.EmailField()
    telefono = models.CharField(max_length=20, null=True, blank=True)
    sitio_web = models.URLField(null=True, blank=True)
    premios = models.TextField(null=True, blank=True)
    created_by= models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)   
    
    #Son los campos que me salen en el admin
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
