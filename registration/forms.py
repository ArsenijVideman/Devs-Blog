from django import forms
from django.contrib.auth.models import User
from .models import Profile, CHOICES
from django.contrib.auth.forms import UserCreationForm


# The UserRegisterForm class is a form used for user registration, including fields for email,
# username, password, password confirmation, and gender.
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        }),
        help_text="You can't type - (@, /, _), etc.",
        max_length=15,
        min_length=5
    )

    email = forms.EmailField(
        label='Email address',
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }),
    )

    password1 = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        }),
        help_text='Password must be at least 8 characters long and must',
        min_length=8,
        max_length=20
    )

    password2 = forms.CharField(
        label='Confrim Password',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confrim Password'
        }),
        help_text='Password must be at least 8 characters long and must',
        min_length=8,
        max_length=20
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1',
                  'password2']


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        }),
        help_text="You can't type - (@, /, _), etc.",
        max_length=15,
        min_length=5
    )

    email = forms.EmailField(
        label='Email address',
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }),
    )

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label='',
        required=False,
        widget=forms.FileInput,
    )

    class Meta:
        model = Profile
        fields = ['img', 'gender', 'agreement']
