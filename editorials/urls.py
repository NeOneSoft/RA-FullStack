from django.urls import path

from . import views

#app_name = 'editorials'
urlpatterns = [
    path('', views.editorials, name='editorials-list'),
    path('new/', views.editorial_new, name='editorial'),
]
