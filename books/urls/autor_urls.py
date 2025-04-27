from django.urls import path # type: ignore
from .views import autores_view, editoriales_view, libros_view, autor_detail, editorial_create, editorial_detail,EditorialList, LibroDeleteView,LibroUpdateView, EditorialDetail, LibrosListView, LibroCreateView, LibroDetailView 


app_name = "books"

urlpatterns = [
    path("autores/", autores_view, name="autor_list"),
    path("autores/<int:id>/", autor_detail, name="autor_detail"),
]
