
# Create your views here.
from django.shortcuts import render # type: ignore

#Vistas generales de la aplicacion
def autores_view(request):
    return render(request, "autores/autores.html")

def editoriales_view(request):    
    return render(request, "editoriales/editoriales.html")

def libros_view(request):
    return render(request, "libros/libros.html")