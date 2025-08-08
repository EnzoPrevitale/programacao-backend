from django.urls import path
from .views import *

urlpatterns = [
    path("authors/", AuthorsView.as_view()),
    path("books/", BooksView.as_view()),
    path("authors/<int:pk>", AuthorsRetrieveUpdateDestroy.as_view()),
    path("books/<int:pk>", BooksRetrieveUpdateDestroy.as_view()),
]