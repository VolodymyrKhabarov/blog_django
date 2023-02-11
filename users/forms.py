from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

User = get_user_model()


class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "id": "username",
        "placeholder": "Username",
        "autofocus": True,
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "id": "password",
        "placeholder": "Password",
    }))


class SignUpForm(UserCreationForm):
    username = forms.CharField(label="Username", min_length=4, max_length=32, widget=forms.TextInput(attrs={
        "class": "form-control",
        "id": "username",
        "placeholder": "Username"
    }))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
        "class": "form-control",
        "id": "email",
        "placeholder": "Email"
    }))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "id": "password",
        "placeholder": "Password",
    }))
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "id": "confirmPassword",
        "placeholder": "Confirm Password",
    }))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
