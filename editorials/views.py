import requests
# djangorestframework
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib import messages

# Models and Serializers
from books.models import Book
from books.serializers import BookSerializer
from .models import Editorial
from .serializers import EditorialSerializer

# Form
from django.shortcuts import render
from .forms import EditorialForm


def editorials(request):
    response = requests.get('http://127.0.0.1:8000/api/v1/editorials')
    editorials = response.json()
    return render(request, 'editorials/editorials_list.html', {"editorials": editorials})


def editorial_new(request):
    form = EditorialForm()
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Editorial was saved successfully')
        else:
            messages.warning(request, 'Error,Editorial was not saved successfully')
    context = {'form': form}
    return render(request, 'editorials/editorial_form.html', context)


class EditorialViewSet(viewsets.ModelViewSet):
    """
    Editorial endpoint(ViewSet)
    """
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    @action(detail=True, methods=['GET'])
    def books(self, request, pk):
        editorial = self.get_object()
        books = Book.objects.filter(editorial__id=editorial.id)
        serialized = BookSerializer(books, many=True)
        if not books:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'This editorial has not books'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)
