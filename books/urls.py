from django.urls import path

from . import views

#app_name = 'books'
urlpatterns = [
    path('', views.books, name='books-list'),
    path('new/', views.book_new, name='book'),
]
