from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="book-home"),
    path('author/', views.authors, name="book-authors"),
    path('bookDetails/<int:received_id>/', views.bookDetails, name="book-details"),
]