from django.urls import path
from apps.authors import views as author_views

urlpatterns = [
    path('authors/', author_views.AuthorAPIView.as_view(), name='authors')
]
