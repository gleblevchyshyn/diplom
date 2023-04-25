from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm
from .models import NewUser
# Create your views here.


def registration(request):
    if request.method == 'POST':
        # form = UserRegistrationForm(request.POST)
        # if form.is_valid():
        #     # Check if the user under this email or phone is already registered
        #     email = form.cleaned_data['email']
        #     phone = form.cleaned_data['phone']
        #     if NewUser.objects.filter(email=email).exists() or NewUser.objects.filter(phone=phone).exists():
        #         messages.error(request, "User with this email or phone already exists!")
        #     else:
        #         user = User(first_name=form.cleaned_data['first_name'],
        #                     second_name=form.cleaned_data['second_name'],
        #                     age=form.cleaned_data['age'],
        #                     sex=form.cleaned_data['sex'],
        #                     phone=form.cleaned_data['phone'],
        #                     email=form.cleaned_data['email'],
        #                     password=form.cleaned_data['password'],
        #                     is_admin=0,
        #                     registration_date=datetime.now(),
        #                     last_visited=datetime.now(),
        #                     cashback=0)
        #         user.save()
        #         messages.success(request, 'Account created successfully!')
                return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')


@login_required
def home(request):
    return render(request, 'home.html')
