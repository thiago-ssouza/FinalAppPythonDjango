from django.shortcuts import render
from .models import Genre, Author, Book, BookInstance

# Create your views here.

def home(request):
    return render(request, 'mylibraray/index.html', {'books' : Book.objects.all() ,'title' : 'Home'})

def authors(request):
    return render(request, 'mylibraray/author_list.html', {'authors' : Author.objects.all(), 'title' : 'Authors'})

def bookDetails(request, received_id):
    bookSelected = Book.objects.get(id=received_id)
    bookIns = BookInstance()
    for bookI in BookInstance.objects.all():
        if bookI.book == bookSelected:
            bookIns = bookI
            break

    return render(request, 'mylibraray/bookInstance.html', {'bookIns' : bookIns, 'bookSelected' : bookSelected ,'title' : 'Details'})