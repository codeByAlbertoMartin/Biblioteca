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

#Definir la accion personalizada
def set_out_of_stock(modeladmin,request, queryset):
    #Actualizar los objetos seleccionados a "publicados"
    queryset.update(is_out_of_stock=True)
    #Mostrar un mensaje informativo en la interfaz de administración
    modeladmin.message_user(request, "Los libros seleccionados han sido marcados como fuera de stock")

#Personalizar el nombre de la acción
set_out_of_stock.short_description = "Marcar libros como fuera de stock"

def export_books_to_csv(modeladmin, request, queryset):
    import csv
    from django.http import HttpResponse

    # Crear la respuesta HTTP con el encabezado adecuado
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'

    # Crear el escritor CSV
    writer = csv.writer(response)
    writer.writerow(['Titulo', 'ISBN', 'Fecha de Publicación', 'Número de páginas', 'Idioma'])

    # Escribir los datos de los libros en el archivo CSV
    for libro in queryset:
        writer.writerow([libro.titulo, libro.isbn, libro.fecha_publicacion, libro.numero_paginas, libro.idioma])

    return response

# Registrar la acción personalizada en el admin
export_books_to_csv.short_description = "Exportar libros seleccionados a CSV"


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo',
                    'isbn',
                    'fecha_publicacion',
                    'numero_paginas',
                    'idioma',
                    'editorial',                   
                    'created_by']
    list_filter = ['editorial', 'idioma', 'is_out_of_stock']
    search_fields = ['titulo', 'autores__nombre']
    filter_horizontal = ['autores']
    actions = [set_out_of_stock, export_books_to_csv]