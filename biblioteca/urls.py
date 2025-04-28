
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from debug_toolbar.toolbar import debug_toolbar_urls # type: ignore
from .views import home_view, contact_view, search_view


urlpatterns = [
    path("", home_view, name="home"),
    path('editorial/', include('books.urls.editorial_urls', namespace="editorial")),
    path('libro/', include('books.urls.libro_urls', namespace="libro")),
    path('autor/', include('books.urls.autor_urls', namespace="autor")),
    path("contacto/", contact_view, name="contacto"),
    path('admin/', admin.site.urls),
    path("buscar/", search_view, name="search")
]+ debug_toolbar_urls()
