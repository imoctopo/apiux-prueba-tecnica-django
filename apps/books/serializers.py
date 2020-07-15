from rest_framework import serializers
from apps.books import models as books_models


class BookSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = books_models.Book
        fields = ['id', 'name', 'isbn']
        depth = 1


class CreateBookSerializer(serializers.ModelSerializer):
    # This field lets check if the author exists without throw an exception if not exists
    author_id = serializers.IntegerField(required=True)

    class Meta:
        model = books_models.Book
        fields = ['id', 'name', 'isbn', 'author_id']
