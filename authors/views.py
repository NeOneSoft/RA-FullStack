# Django
from django.contrib import messages
from django.views.generic import ListView, DetailView

# djangorestframework
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Models and Serializers
from authors.models import Author
from authors.serializers import AuthorSerializer
from books.models import Book
from books.serializers import BookSerializer

# Form
from django.shortcuts import render
from .forms import AuthorForm


def authors(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'authors/authors_list.html', context)


class AuthorListView(ListView):
    model = Author
    template_name = 'authors/authors_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'authors'
    ordering = ['-first_name']
    paginate_by = 5


# Data for Template
class AuthorDetailView(DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the commits
        context['books'] = Book.objects.filter(authors=self.object)
        return context


def author_new(request):
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Author was saved successfully')
        else:
            messages.warning(request, 'Error, Author was not saved successfully')
    context = {'form': form}
    return render(request, 'authors/author_form.html', context)


# API djangorestframework Author
class AuthorViewSet(viewsets.ModelViewSet):
    """
    Author endpoint(ViewSet)
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @action(detail=True, methods=['GET'])  # Define detail and method
    def books(self, request, pk=None):  # Decorator action
        author = self.get_object()  # Get self object
        books = Book.objects.filter(authors__id=author.id)  # Get objects related to author id
        serialized = BookSerializer(books, many=True)  # Get serialized books data
        if not books:  # Send a status
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'This book has not authors'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)
