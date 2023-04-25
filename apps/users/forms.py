from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import NewUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=254)
    username = forms.CharField(required=True, max_length=30)

    class Meta:
        model = NewUser
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2', 'age', 'sex', 'phone')


class LoginForm(AuthenticationForm):
    class Meta:
        model = NewUser
        fields = ('email', 'password')
