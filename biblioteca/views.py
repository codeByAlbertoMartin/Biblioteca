from django.utils import translation
from django.http import HttpResponseRedirect
from django.conf import settings

from django.shortcuts import render
from django.views.generic import View # type: ignore

from books.forms import SearchForm
from .form import ContactForm
from books.models import Autor, Libro, Editorial

from django.contrib import messages
from django.utils.translation import gettext as _
from django.utils.translation import get_language


#Vistas generales de  la aplicacion
def home_view(request):
    messages.error(request, _("Formulario enviado correctamente"))
    print("IDIOMA ACTUAL:", get_language())  
    return render(request, "general/home.html")

# def contact_view(request):
#     if request.POST:
#         email= request.POST["email"]
#         nombre= request.POST["nombre"]        
#         comentario= request.POST["comentario"]
#         print(f'Se ha enviado un correo a {email}, de {nombre} con el siguiente comentario {comentario}')
#     return render(request, "general/contacto.html")


# def search_view(request):
#     if request.GET: #No hemos protegido de los formularios, ya lo veremos en otro momento
#         busqueda = request.GET["q"]
#         autores = Autor.objects.filter(nombre__icontains=busqueda)
#         editoriales = Editorial.objects.filter(nombre__icontains=busqueda)
#         libros = Libro.objects.filter(titulo__icontains=busqueda)
#         context = {
#             "autores": autores,
#             "editoriales": editoriales,
#             "libros": libros,
#         }
#         return render(request, "general/search.html", context)
#     return render(request, "general/search.html")

def search_view(request):
    if request.GET:
        formulario = SearchForm(request.GET)

        busqueda = formulario.data["q"]
        autores = Autor.objects.filter(nombre__icontains=busqueda)
        editoriales = Editorial.objects.filter(nombre__icontains=busqueda)
        libros = Libro.objects.filter(titulo__icontains=busqueda)
        context = {
            "autores": autores,
            "editoriales": editoriales,
            "libros": libros,
            "formulario": formulario
        }
        return render(request, "general/search.html", context)
    else:
        formulario = SearchForm()
        context = {
            "formulario": formulario
        }
        return render(request, "general/search.html", context)

def contact_view(request):
    #La request es lo que se envia por el formulario una vez que se pincha en el boton
    if request.POST:
        formulario = ContactForm(request.POST)

        if formulario.is_valid(): #SI CUMPLE CON LOS REQUISITOS DEL FORMS.PY
            email= formulario.cleaned_data["email"]
            nombre= formulario.cleaned_data["nombre"] 
            comentario= formulario.cleaned_data["comentario"]
            print(f'Se ha enviado un correo a {email}, de {nombre} con el siguiente comentario {comentario}')
            context = {
                "formulario": formulario,
                "success": True,
            }
            messages.info(request, "Formulario enviado correctamente") #De esta forma el mensaje se puede ver una vez solamente, que es lo que se quiere
            return render(request, "general/contacto.html", context)
        else: 
            context = {
                "formulario": formulario
            }
            return render(request, "general/contacto.html", context)

    formulario = ContactForm() 
    context = {
        "formulario": formulario
    }
    return render(request, "general/contacto.html", context)