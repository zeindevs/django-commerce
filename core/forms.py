from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your username",
                "class": "w-full py-2 px-4 rounded-md",
            }
        )
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your email address",
                "class": "w-full py-2 px-4 rounded-md",
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Your password",
                "class": "w-full py-2 px-4 rounded-md",
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Repeat your password",
                "class": "w-full py-2 px-4 rounded-md",
            }
        )
    )
