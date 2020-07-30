# Forms
from django.forms import ModelForm

# Models
from .models import Author


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'birth_date', 'phone']
