from faker import Faker
from apps.authors import models as author_models


def list_authors():
    """Lists all authors"""
    return author_models.Author.objects.all()


def get_author(pk):
    """Returns an author or none if not exists"""
    try:
        return author_models.Author.objects.get(pk=pk)
    except:
        return None


def create_fake_author():
    """Creates a fake author and returns it"""
    fake_author = Faker()
    author = author_models.Author()
    author.name = fake_author.name()
    author.nationality = fake_author.country()
    author.save()
    return author
