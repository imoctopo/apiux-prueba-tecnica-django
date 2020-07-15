from django.urls import path
from apps.books import views as books_views

urlpatterns = [
    path('books/', books_views.BookAPIView.as_view(), name='books')
]
