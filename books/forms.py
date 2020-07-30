# Forms
from django.forms import ModelForm

# Models
from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'editorial', 'date_pub']
