from rest_framework import serializers
from apps.books import models as books_models


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = books_models.Book
        fields = '__all__'
