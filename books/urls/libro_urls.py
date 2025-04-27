from django.urls import path # type: ignore
from .views import autores_view, editoriales_view, libros_view, autor_detail, editorial_create, editorial_detail,EditorialList, LibroDeleteView,LibroUpdateView, EditorialDetail, LibrosListView, LibroCreateView, LibroDetailView 


app_name = "books"

urlpatterns = [
    path("libros/",LibrosListView.as_view(), name="libros_list"),
    path("libros/nuevo/", LibroCreateView.as_view(), name="libro_create"),
    path("libro/<pk>/", LibroDetailView.as_view(), name="libro_detail"),
    path("libro/editar/<pk>", LibroUpdateView.as_view(), name="libro_update"),
    path("libro/eliminar/<pk>", LibroDeleteView.as_view(), name="libro_delete"),
]
