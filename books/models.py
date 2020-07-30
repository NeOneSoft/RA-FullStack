# Django
from django.db import models
from django.utils import timezone

from authors.models import Author
from editorials.models import Editorial


class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)
    authors = models.ManyToManyField(Author)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    date_pub = models.DateField('Publication date', default=timezone.now())

    def __str__(self):
        return self.title
