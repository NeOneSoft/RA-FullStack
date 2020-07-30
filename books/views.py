# Django
import requests

# djangorestframework
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib import messages

# Models and Views
from authors.serializers import AuthorSerializer
from editorials.serializers import EditorialSerializer
from .models import Book
from .serializers import BookSerializer, CreateBookSerializer

# Form
from django.shortcuts import render
from .forms import BookForm


# Django Front-End section
def books(request):
    response = requests.get('http://127.0.0.1:8000/api/v1/books')
    books = response.json()
    return render(request, 'books/books_list.html', {"books": books})


def book_new(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book was saved successfully')
        else:
            messages.warning(request, 'Error,Book was not saved successfully')
    context = {'form': form}
    return render(request, 'books/book_form.html', context)


# Django rest_framework section
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Over write our serializer class
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateBookSerializer
        return BookSerializer

    # Detail for authors
    @action(detail=True, methods=['GET'])
    def authors(self, request, pk):
        books = self.get_object()
        authors = books.authors.all()
        serialized = AuthorSerializer(authors, many=True)
        if not authors:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'This book has no authors'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    # Detail for editorial
    @action(detail=True, methods=['GET'])
    def editorial(self, request, pk):
        books = self.get_object()
        editorial = books.editorial
        serialized = EditorialSerializer(editorial)
        if not editorial:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'This book has not editorial'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)
