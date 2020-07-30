# djangorestframework
from rest_framework import serializers

# Models
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    """
    General purpose
    """
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'birth_date', 'phone')
