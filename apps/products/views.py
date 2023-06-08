from django.shortcuts import render

from django.apps import apps
from .models import *
from django.core.paginator import Paginator


def book_list(request):
    book_list = Book.objects.defer('content').only('idbook', 'title', 'price', 'average_rating',
                                                   'cover_img')  # defer the 'content' field
    paginator = Paginator(book_list, 28)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    return render(request, 'book_list.html', {'books': books})


def book_detail(request, book_id):
    rec_sys = apps.get_app_config('recommendations').recommendation_system
    book = Book.objects.select_related('language_idlanguage', 'discount_iddiscount', 'format_idformat').get(
        idbook=book_id)
    ids = rec_sys.get_similar_books(book_index=book.idbook)
    books = Book.objects.filter(idbook__in=ids)
    print(books)
    return render(request, 'book_detail.html', {'book': book, 'books':books})

