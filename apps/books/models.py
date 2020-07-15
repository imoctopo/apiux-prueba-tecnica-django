from django.db import models


class Book(models.Model):
    author = models.ForeignKey('authors.Author', on_delete=models.PROTECT, related_name='books')
    name = models.CharField(max_length=30)
    isbn = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"{self.name} - {self.author} [{self.isbn}]"
