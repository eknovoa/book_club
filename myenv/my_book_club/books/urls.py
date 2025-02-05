from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books, name='books'),
    path('database/', views.database, name="database"),
    path('poll/', views.poll, name='poll'),
]
