from import_export import resources
from django.contrib import admin

from books.models import Autor, Editorial, Libro
from import_export.admin import ImportExportModelAdmin

class LibroInline(admin.TabularInline):
    model = Libro

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'fecha_nacimiento']
        export_order = ['nombre', 'apellido', 'fecha_nacimiento']
        
# Register your models here.
@admin.register(Autor)
class AutorAdmin(ImportExportModelAdmin):
    resource_class = AutorResource
    #Para los campos que quiero que se vean en el admin
    list_display = ['nombre',
                    'apellido',
                    'fecha_nacimiento',
                    'email',
                    'telefono', 
                    'created_by']
    

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ['nombre',
                    'ciudad',
                    'telefono',
                    'email',
                    'sitio_web',
                    'fecha_fundacion',
                    'created_by']
    list_filter = ['fecha_fundacion'] 
    ordering = ["nombre"]
    inlines = [
        LibroInline,
    ]

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo',
                    'isbn',
                    'fecha_publicacion',
                    'numero_paginas',
                    'idioma',
                    'editorial',                   
                    'created_by']
    list_filter = ['editorial', 'idioma']
    search_fields = ['titulo', 'autores__nombre']
    filter_horizontal = ['autores']
    