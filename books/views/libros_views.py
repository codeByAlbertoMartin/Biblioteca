# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from books.models import Libro
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView



class LibroListView(ListView):
    model= Libro
    template_name="libros/LibroList.html"
    context_object_name="libros"


class LibroDetailView(DetailView):
    model= Libro
    template_name = "libros/LibroDetail.html"
    context_object_name = "libro"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        return context
    

class LibroCreateView(CreateView):
    model= Libro
    fields = [
        'titulo', 'isbn','fecha_publicacion','numero_paginas',
        'idioma', 'descripcion', 'editorial', 'autores',
        'genero','precio'
    ]
    template_name="libros/LibroCreate.html"
    success_url=reverse_lazy("libro:list")

    def form_valid(self, form):
        #Definimos que el campo created_by sea el usuario que esta realizando la request
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class LibroUpdateView(UpdateView):
    model= Libro    
    fields = [
        'titulo', 'isbn','fecha_publicacion','numero_paginas',
        'idioma', 'descripcion', 'editorial', 'autores',
        'genero','precio'
    ]
    template_name="libros/LibroUpdate.html"
    success_url=reverse_lazy("libro:list")


class LibroDeleteView(DeleteView):
    model= Libro
    template_name="libros/LibroDelete.html"
    success_url=reverse_lazy("libro:list")
