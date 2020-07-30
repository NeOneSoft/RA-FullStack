# Django
from django.db import models
from django.urls import reverse


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name
