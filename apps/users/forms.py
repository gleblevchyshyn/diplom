from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import NewUser


# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(required=True, max_length=254)
#     username = forms.CharField(required=True, max_length=30)
#
#     class Meta:
#         model = NewUser
#         fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2', 'age', 'sex', 'phone')


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}))
    sex = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Sex'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}))

    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get('phone')
        if phone and NewUser.objects.filter(phone=phone).exists():
            raise forms.ValidationError("A user with that phone already exists.")

    class Meta:
        model = NewUser
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2', 'age', 'sex', 'phone')


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))