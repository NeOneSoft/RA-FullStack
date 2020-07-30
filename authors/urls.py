from django.urls import path

from . import views
from .views import AuthorListView, AuthorDetailView

#app_name = 'authors'
urlpatterns = [
    path('', AuthorListView.as_view(), name='authors-list'),
    path('<int:pk>/', AuthorDetailView.as_view(), name='authors-detail'),
    path('new/', views.author_new, name='authors-new'),
]
