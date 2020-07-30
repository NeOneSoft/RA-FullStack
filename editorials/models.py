# Django
from django.db import models


class Editorial(models.Model):
    name_ed = models.CharField(max_length=200)
    direction = models.CharField(max_length=200)
    web_page = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.name_ed
