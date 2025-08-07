from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Author
from .serializers import AuthorSerializers

class AuthorsView(ListCreateAPIView):
    
