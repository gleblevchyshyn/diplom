from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect


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
    book = Book.objects.select_related('language_idlanguage', 'discount_iddiscount', 'format_idformat').get(
        idbook=book_id)
    return render(request, 'book_detail.html', {'book': book})

