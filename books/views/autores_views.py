from django.shortcuts import render
from datetime import date
from books.models import Autor
#Vistas generales de la aplicacion
def autores_view(request):
    autores = Autor.objects.all()
    context = {
        'autores': autores,
    }
    return render(request, "autores/autores.html", context)

def autor_detail(request, id):
    print(id)
    autores = [
        {
            'id': 1,
            'nombre': 'Gabriel Garcia Marquez',
            'fec_nac': date(1980,8,1)
        },
        {
            'id': 2,
            'nombre': 'Rafael Alberti',
            'fec_nac': date(1985,10,5)
        },
        {
            'id': 3,
            'nombre': 'Gustavo Adolfo Becquer',
            'fec_nac': date(1999,11,2)
        }
    ]
    context = {
        "autor": None
        }
    for autor in autores:
        if autor["id"] ==id:
            context["autor"] = autor
    return render(request, "autores/autor_detail.html", context)