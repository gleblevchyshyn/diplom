from django import forms


class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    second_name = forms.CharField(max_length=20)
    age = forms.IntegerField(min_value=0, max_value=120)
    sex = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
    phone = forms.CharField(max_length=15)
    email = forms.EmailField()
    password = forms.CharField(max_length=16, widget=forms.PasswordInput)


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=16, widget=forms.PasswordInput)
