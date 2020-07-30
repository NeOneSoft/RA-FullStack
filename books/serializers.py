# djangorestframework
from rest_framework import serializers

# Models
from .models import Book
from authors.serializers import AuthorSerializer
from editorials.serializers import EditorialSerializer


class BookSerializer(serializers.ModelSerializer):
    """
    General purpose
    """
    authors = AuthorSerializer(many=True, read_only=True)
    editorial = EditorialSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ('title', 'authors', 'editorial', 'date_pub')


class CreateBookSerializer(serializers.ModelSerializer):
    """
    Create Book Serializer with out related fields
    """

    class Meta:
        model = Book
        fields = ('title', 'authors', 'editorial', 'date_pub')
