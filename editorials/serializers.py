# djangorestframework
from rest_framework import serializers

# Models
from .models import Editorial


class EditorialSerializer(serializers.ModelSerializer):
    """
    General Pourpose
    """

    class Meta:
        model = Editorial
        fields = ('name_ed', 'direction', 'web_page', 'city')
