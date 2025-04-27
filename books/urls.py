from django.urls import path, include # type: ignore


app_name = "books"

urlpatterns = [ 
    path('editorial/', include('books.urls.editorial_url')),
    # path('libro/', include('books.urls.libro_url')),
    # path('autor/', include('books.urls.autor_url')),
    
]
