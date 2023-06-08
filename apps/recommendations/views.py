from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps
from ..products.models import *


def top_books(request):
    rec_sys = apps.get_app_config('recommendations').recommendation_system
    ids = rec_sys.top_100_books_ids
    books = Book.objects.filter(idbook__in=ids)
    return render(request, 'book_list.html', {'books': books})


def search(request):
    rec_sys = apps.get_app_config('recommendations').recommendation_system
    if request.method == 'POST':
        query = request.POST.get('query', '')
        query = rec_sys.clean_text(query)
        ids = rec_sys.search(query)
        books = Book.objects.filter(idbook__in=ids)
        return render(request, 'book_list.html', {'books': books})


@login_required
def personal_recs(request):
    user_id = request.user.id
    rec_sys = apps.get_app_config('recommendations').recommendation_system
    ids = rec_sys.predict(user_id)
    books = Book.objects.filter(idbook__in=ids)
    return render(request, 'book_list.html', {'books': books})
