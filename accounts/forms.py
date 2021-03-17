from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

        # '''
        # widgets = {
        #     'first_name': forms.TextInput(attrs={'class': 'form-control py-3', 'style': 'height: 50px;', 'placeholder': 'Your First Name'}),
        #     'last_name': forms.TextInput(attrs={'class': 'form-control py-3', 'style': 'height: 50px;', 'placeholder': 'Your Last Name'}),
        #     'username': forms.TextInput(attrs={'class': 'form-control input', 'style': 'height: 50px;', 'placeholder': 'Your Username'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control input', 'style': 'height: 50px;', 'placeholder': 'Your Email'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'input', 'style': 'height: 50px;', 'placeholder': 'Your Password'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'input py-3', 'style': 'height: 50px;', 'placeholder': 'Re-type Password'}),
        # }
        # '''