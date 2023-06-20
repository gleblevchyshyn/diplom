from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.apps import apps
from .models import *
from django.core.paginator import Paginator
from ..users.models import Rewiev
from django.utils import timezone


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

    user = request.user

    # Get the user's rating for the book if it exists
    if user.is_authenticated:
        try:
            review = Rewiev.objects.get(user_iduser=user, book_idbook=book)
            user_rating = review.rating
        except Rewiev.DoesNotExist:
            user_rating = None
    else:
        user_rating = None

    if request.method == 'POST':
        rating = request.POST.get('rating')
        if rating:
            # Create or update the user's review for the book
            review, created = Rewiev.objects.update_or_create(
                user_iduser=user,
                book_idbook=book,
                defaults={'rating': rating, 'review_date': timezone.now()},
            )
            response_data = {'success': True}
            return JsonResponse(response_data)
        else:
            response_data = {'success': False, 'message': 'Invalid rating value'}
            return JsonResponse(response_data)

    return render(request, 'book_detail.html', {'book': book, 'books': books, 'review': user_rating})



