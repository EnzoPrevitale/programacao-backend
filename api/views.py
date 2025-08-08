from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *

class AuthorsView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers

class BooksView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorsRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers

class BooksRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

