from django.urls import path # type: ignore
from books.views.autores_views import AutorListView, AutorDetailView, AutorCreateView, AutorDeleteView, AutorUpdateView
app_name = "autor"

urlpatterns = [
    path("list/", AutorListView.as_view(), name="list"),
    path("detail/<pk>", AutorDetailView.as_view(), name="detail"),
    path("create/", AutorCreateView.as_view(), name="create"),
    path("delete/<pk>", AutorDeleteView.as_view(), name="delete"),
    path("update/<pk>", AutorUpdateView.as_view(), name="update"),  
]