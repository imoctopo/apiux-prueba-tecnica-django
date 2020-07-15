from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from apps.authors import dao as author_dao
from apps.authors import serializers as author_serializers


@api_view(['GET', 'POST'])
def list_or_create_authors(request):
    """Lists and creates an author"""

    # Action for POST
    if request.method == 'POST':
        author = author_serializers.AuthorSerializer(data=request.data)
        if author.is_valid():
            author.save()
            return Response({
                'author': author.data
            })
        return Response({
            'errors': author.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    # Action for GET
    authors = author_dao.list_authors()
    return Response({
        'authors': author_serializers.AuthorSerializer(authors, many=True).data
    })


@api_view(['GET'])
def get_author(request, pk):
    """Returns an author or 404"""
    author = get_object_or_404(author_dao.author_models.Author, pk=pk)
    return Response({
        'author': author_serializers.AuthorSerializer(author).data
    })
