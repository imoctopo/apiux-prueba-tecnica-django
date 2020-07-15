from rest_framework import serializers
from apps.authors import models as authors_models
from apps.books import serializers as books_serializers


class AuthorSerializer(serializers.ModelSerializer):
    """Book uses its serializer in order to hide the author field"""
    books = books_serializers.BookSerializer(many=True, required=False)

    class Meta:
        model = authors_models.Author
        fields = ['id', 'name', 'nationality', 'books']
