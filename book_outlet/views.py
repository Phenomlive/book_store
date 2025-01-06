from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Avg

# Create your views here.

def index(request):
    books = Book.objects.all()
    num_books = books.count()
    avg_rating = books.aggregate(Avg('rating'))
    return render(request, 'book_outlet/index.html', {
        'books': books,
        'num_books': num_books,
        'avg_rating': avg_rating
    })

def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(id=id)
    # except:
    #     raise Http404

    book = get_object_or_404(Book, slug=slug)
    
    return render(request, 'book_outlet/book-detail.html', {
        'title': book.title,
        'author': book.author,
        'rating': book.rating,
        'is_bestselling': book.is_bestselling
    })