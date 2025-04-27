from django.urls import path # type: ignore
from books.view import EditorialListView, EditorialDetailView, EditorialCreateView, EditoriaDeleteView, EditorialUpdateView

app_name = "books"

urlpatterns = [   
    path("list/", EditorialListView.as_view(), name="editorial_lista"),
    path("detail/<pk>", EditorialDetailView.as_view(), name="editorial_lista"),
    path("create/", EditorialCreateView, name="editorial_create"),
    path("delete/<pk>", EditoriaDeleteView, name="editorial_delete"),
    path("update/<pk>", EditorialUpdateView.as_view(), name="editorial_update"),    
]
