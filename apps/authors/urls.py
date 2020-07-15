from django.urls import path
from apps.authors import views as author_views


urlpatterns = [
    path('', author_views.list_or_create_authors, name='list_or_create_authors'),
    path('<int:pk>/', author_views.get_author, name='get_author'),
]
