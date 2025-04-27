
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from debug_toolbar.toolbar import debug_toolbar_urls # type: ignore
from .views import home_view, contact_view, search_view


urlpatterns = [
    path("", home_view, name="home"),
    path("", include('books.urls', namespace="books")),#Tiene que coincidir con el nombre de la app en el fichero de urls.py de la app books
    path("contacto/", contact_view, name="contacto"),
    path('admin/', admin.site.urls),
    path("buscar/", search_view, name="search")
]+ debug_toolbar_urls()
