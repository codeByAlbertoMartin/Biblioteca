from datetime import datetime
from books.models import Libro, Editorial, Autor

def  get_current_year_context_processor(request):
    current_year = datetime.now().year 
    #Importante devolver un diccionario
    return {
        'current_year': current_year
    }

def get_statistic_books(request):
    return {
        'n_libros': Libro.objects.all().count(),
        'n_autores': Autor.objects.all().count(),
        'n_editoriales': Editorial.objects.all().count(),
        'user_logged': request.user
    }
