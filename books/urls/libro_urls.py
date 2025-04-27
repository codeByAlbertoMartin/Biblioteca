from django.urls import path # type: ignore
from books.views.libros_views import LibroCreateView, LibroDeleteView, LibroDetailView, LibroListView, LibroUpdateView
app_name = "libro"

urlpatterns = [
    path("list/", LibroListView.as_view(), name="list"),
    path("detail/<pk>", LibroDetailView.as_view(), name="detail"),
    path("create/", LibroCreateView.as_view(), name="create"),
    path("delete/<pk>", LibroDeleteView.as_view(), name="delete"),
    path("update/<pk>", LibroUpdateView.as_view(), name="update"),  
]
