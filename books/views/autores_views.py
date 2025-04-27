
from books.models import Autor
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
#Vistas generales de la aplicacion


class AutorListView(ListView):
    model= Autor
    template_name="autores/AutorList.html"
    context_object_name="libros"


class AutorDetailView(DetailView):
    model= Autor
    template_name = "autores/AutorDetail.html"
    context_object_name = "libro"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        return context
    

class AutorCreateView(CreateView):
    model= Autor
    fields = [
        'nombre','apellido', 'fecha_nacimiento',
        'nacionalidad','biografia','email', 'telefono',
        'sitio_web','premios'
    ]
    template_name="autores/AutorCreate.html"
    success_url=reverse_lazy("books:autores_list")


class AutorUpdateView(UpdateView):
    model= Autor
    fields = [
        'titulo',
        'isbn',
        'fecha_publicacion',
        'numero_paginas'

    ]
    template_name="autores/AutorUpdate.html"
    success_url=reverse_lazy("books:autores_list")


class AutorDeleteView(DeleteView):
    model= Autor
    template_name="autores/AutorDelete.html"
    success_url=reverse_lazy("books:autores_list")
