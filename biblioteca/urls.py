
from django.contrib import admin # type: ignore
from django.urls import path, include, re_path# type: ignore
from debug_toolbar.toolbar import debug_toolbar_urls # type: ignore
from .views import home_view, contact_view, search_view
from django.conf.urls.i18n import set_language
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings


from . import views
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # para set_language
] + debug_toolbar_urls()

urlpatterns += i18n_patterns(
    path('set-language/', set_language, name='set_language'),
    path("", home_view, name="home"),
    path('editorial/', include('books.urls.editorial_urls', namespace="editorial")),
    path('libro/', include('books.urls.libro_urls', namespace="libro")),
    path('autor/', include('books.urls.autor_urls', namespace="autor")),
    path("contacto/", contact_view, name="contacto"),
    path('admin/', admin.site.urls),
    path("buscar/", search_view, name="search")
)


if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/', include('rosetta.urls'))
    ]