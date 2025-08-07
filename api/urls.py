from django.urls import path
from views import *

urlpatterns = [
    path("authors/", AuthorsView.as_view())
]