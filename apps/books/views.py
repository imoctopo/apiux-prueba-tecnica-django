from django.db import transaction
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.authors import dao as author_dao
from apps.books import serializers as book_serializers


@api_view(['POST'])
@transaction.atomic
def create_books(request):
    """Creates a book"""
    book = book_serializers.CreateBookSerializer(data=request.data)
    if book.is_valid():
        author_id = book.validated_data['author_id']
        author = author_dao.get_author(author_id) or author_dao.create_fake_author()  # Returns an author's instance or create a new one and returns its instance
        book.validated_data['author_id'] = author.pk
        book.save()
        return Response({
            'book': book.data
        })
    return Response({
        'errors': book.errors
    }, status=status.HTTP_400_BAD_REQUEST)
