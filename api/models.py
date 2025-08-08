from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=30, null=True, blank=True)
    biography = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=0)
    release_date = models.DateField(null=True, blank=True)
    country = models.CharField(null=True, blank=True)
    synopsis = models.TextField(null=True, blank=True)
