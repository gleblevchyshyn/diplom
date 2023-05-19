from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import json

# Create your views here.
from .models import *

from django.core.cache import cache

from django.contrib.auth.decorators import user_passes_test

from django.core.paginator import Paginator


def book_list(request):
    book_list = Book.objects.defer('content').only('idbook', 'title', 'price', 'average_rating', 'cover_img')  # defer the 'content' field
    paginator = Paginator(book_list, 28)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    return render(request, 'book_list.html', {'books': books})


def book_detail(request, book_id):
    book = Book.objects.select_related('language_idlanguage', 'discount_iddiscount', 'format_idformat').get(idbook=book_id)
    return render(request, 'book_detail.html', {'book': book})
