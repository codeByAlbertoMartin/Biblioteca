#Vistas generales de la aplicacion
from django.urls import reverse_lazy
from books.models import Editorial
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from books.decorators import user_can_delete_editorial

class EditorialListView(ListView):
    model=Editorial
    template_name = "editoriales/EditorialList.html"
    context_object_name= "editoriales" #por defecto es object_list, que en el template sería lo que tendriamos que poner al hacer el for


class EditorialDetailView(DetailView):
    model= Editorial
    template_name = "editoriales/EditorialDetail.html"
    context_object_name = "editorial"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["titulo"] = "Este es un titulo de vistas basadas en clases"
        return context
    

@method_decorator(login_required, name="dispatch")
class EditorialCreateView(CreateView):
    model= Editorial
    fields = [
        'nombre','direccion','ciudad','estado',
        'pais','codigo_postal','telefono',
        'email','sitio_web','fecha_fundacion',
    ]
    template_name="editoriales/EditorialCreate.html"
    success_url=reverse_lazy("editorial:list")

    def form_valid(self, form):
        #Definimos que el campo created_by sea el usuario que esta realizando la request
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(user_can_delete_editorial, name="dispatch")
class EditorialUpdateView(UpdateView):
    model= Editorial
    fields = [
        'nombre','direccion','ciudad','estado',
        'pais','codigo_postal','telefono',
        'email','sitio_web','fecha_fundacion',
    ]
    template_name="editoriales/EditorialUpdate.html"
    success_url=reverse_lazy("editorial:list")

    
@method_decorator(user_can_delete_editorial, name="dispatch")
class EditorialDeleteView(DeleteView):
    model= Editorial
    template_name="editoriales/EditorialDelete.html"
    success_url=reverse_lazy("editorial:list")