from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, LoginForm
from ..products.models import Book
from .models import Wishlist


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('user_login')


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def add_to_wishlist(request, book_id):
    book = Book.objects.get(idbook=book_id)
    user = request.user

    wishlist, created = Wishlist.objects.update_or_create(
        user_iduser=user, book_idbook=book
    )

    # Return a JSON response indicating the success or failure of the operation
    response_data = {'message': 'Book added to wishlist'}
    return JsonResponse(response_data)


@login_required
def wishlist(request):
    user = request.user
    wishlist_items = Wishlist.objects.filter(user_iduser=user)

    context = {
        'wishlist_items': wishlist_items
    }
    return render(request, 'wishlist.html', context)