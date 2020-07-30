from django.contrib import admin
from .models import Editorial


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('name_ed', 'direction', 'web_page', 'city')
