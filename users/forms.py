"User application forms"

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError

from users.models import UserModel


class SignUpForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("username", "email",
                  "password", "confirm_password")

