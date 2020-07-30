# Django and djangorestframework
from django.conf.urls import url, include
from rest_framework import routers

# Views
from authors.views import AuthorViewSet
from books.views import BookViewSet
from editorials.views import EditorialViewSet

# API urls
router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'editorials', EditorialViewSet)
router.register(r'books', BookViewSet)


urlpatterns = [
    url(r'', include(router.urls))
]
