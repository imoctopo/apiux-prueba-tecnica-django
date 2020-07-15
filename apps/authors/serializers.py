from rest_framework import serializers
from apps.authors import models as authors_models


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = authors_models.Author
        fields = '__all__'
