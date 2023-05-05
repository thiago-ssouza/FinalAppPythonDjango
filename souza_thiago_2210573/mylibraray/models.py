from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Author(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    birthDate = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.lastName+ ', ' + self.firstName

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    summary = models.TextField()
    isbn = models.CharField(max_length=13)
    genre = models.ManyToManyField(Genre)

    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return str(self.title)

class BookInstance(models.Model):

    B_STATUS = [('M','Maintenance'), ('B','Booked'), ('A', 'Available'), ('R','Reserved')]
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=B_STATUS, default='A')
    due = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['book']
    
    def __str__(self):
        return str(self.book)

