from django.urls import path
from apps.books import views as books_views

urlpatterns = [
    path('', books_views.create_books, name='create_books')
]
