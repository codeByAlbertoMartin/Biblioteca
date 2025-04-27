from django.urls import path # type: ignore
from books.views.editoriales_views import EditorialListView, EditorialDetailView, EditorialCreateView, EditorialDeleteView, EditorialUpdateView

app_name = "editorial"

urlpatterns = [   
    path("list/", EditorialListView.as_view(), name="lista"),
    path("detail/<pk>", EditorialDetailView.as_view(), name="detail"),
    path("create/", EditorialCreateView.as_view(), name="create"),
    path("delete/<pk>", EditorialDeleteView.as_view(), name="delete"),
    path("update/<pk>", EditorialUpdateView.as_view(), name="update"),    
]
