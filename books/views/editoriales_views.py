#Vistas generales de la aplicacion
from django.shortcuts import render, redirect# type: ignore
from django.urls import reverse
from books.forms import EditorialCreate, EditorialModelFormCreate
from books.models import Editorial
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class EditorialList(ListView):
    model=Editorial
    template_name = "editoriales/editoriales_ccbv.html"
    context_object_name= "editoriales" #por defecto es object_list, que en el template sería lo que tendriamos que poner al hacer el for

class EditorialDetail(DetailView):
    model= Editorial
    template_name = "editoriales/editorial_detail_ccbv.html"
    context_object_name = "editorial"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["titulo"] = "Este es un titulo de vistas basadas en clases"
        return context
    

def editoriales_view(request):
    editoriales = Editorial.objects.all()
    context = {
        'editoriales': editoriales,
    }
    return render(request, "editoriales/editoriales.html", context)

def editorial_create(request):
    if request.POST:
        form = EditorialModelFormCreate(request.POST)
        if form.is_valid():
            nueva_editorial = Editorial.objects.create(
                nombre = form.cleaned_data["nombre"],              
                direccion = form.cleaned_data["direccion"],
                ciudad = form.cleaned_data["ciudad"],
                pais = form.cleaned_data["pais"],
                codigo_postal = form.cleaned_data["codigo_postal"],
                telefono = form.cleaned_data["telefono"],
                email = form.cleaned_data["email"],
                sitio_web = form.cleaned_data["sitio_web"],
                fecha_fundacion = form.cleaned_data["fecha_fundacion"],
            )
            # Redireccionar a la vista detalle de la nueva editorial creada
            return redirect(reverse('books:editorial_detail', kwargs={"id": nueva_editorial.pk}))
    else:
        form = EditorialModelFormCreate()
    context = {
        "form": form
    }
    return render(request, "editoriales/editorial_create.html", context)

def editorial_detail(request, id):
    editorial = Editorial.objects.get(pk=id)
    print(editorial)
    context = {
        "editorial": editorial
        }
    return render(request, "editoriales/editorial_detail.html", context)