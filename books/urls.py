from django.urls import path # type: ignore
from .views import autores_view, editoriales_view, libros_view, autor_detail, editorial_create, editorial_detail,EditorialList, LibroDeleteView,LibroUpdateView, EditorialDetail, LibrosListView, LibroCreateView, LibroDetailView 


app_name = "books"

urlpatterns = [
    
    path("autores/", autores_view, name="autor_list"),
    path("autores/<int:id>/", autor_detail, name="autor_detail"),
    
    path("editoriales/create", editorial_create, name="editorial_create"),
    path("editoriales/", editoriales_view, name="editorial_list"),
    path("editoriales/lista", EditorialList.as_view(), name="editorial_lista_ccbv"),
    path("editoriales/detalle/<int:id>/", editorial_detail, name="editorial_detail"),
    path("editoriales/detalle/ccbv/<pk>/", EditorialDetail.as_view(), name="editorial_detail_ccbv"),
    
    path("libros/",LibrosListView.as_view(), name="libros_list"),
    path("libros/nuevo/", LibroCreateView.as_view(), name="libro_create"),
    path("libro/<pk>/", LibroDetailView.as_view(), name="libro_detail"),
    path("libro/editar/<pk>", LibroUpdateView.as_view(), name="libro_update"),
    path("libro/eliminar/<pk>", LibroDeleteView.as_view(), name="libro_delete"),
    
]
