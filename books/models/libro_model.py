from django.db import models
from .autor_model import Autor
from .editorial_model import Editorial
from django.contrib.auth.models import User


# Modelo para Libros
class Libro(models.Model):
    titulo = models.CharField(max_length=300)
    isbn = models.CharField(max_length=13, unique=True)
    fecha_publicacion = models.DateField()
    numero_paginas = models.IntegerField()

    LANG_CHOICES = {
        'ES': 'Español',
        'EN': 'Inglés',
    }

    idioma = models.CharField(max_length=2, choices=LANG_CHOICES, default='ES')
    descripcion = models.TextField(null=True, blank=True)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, null=True, blank=True)
    autores = models.ManyToManyField(Autor)
    genero = models.CharField(max_length=100, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2,  null=True, blank=True)
    created_by= models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    is_out_of_stock = models.BooleanField(verbose_name ="Esta fuera de stock", default=False)
    
    def __str__(self):
        return self.titulo
    
