# Forms
from django.forms import ModelForm

# Models
from .models import Editorial


class EditorialForm(ModelForm):
    class Meta:
        model = Editorial
        fields = ['name_ed', 'direction', 'web_page', 'city']
