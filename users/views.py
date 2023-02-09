from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout

from users.models import UserModel
from users.forms import SignUpForm


def signin_view(request: HttpRequest):

    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            form.save()
            redirect_url = reverse_lazy("signin")
            return HttpResponseRedirect(redirect_url)
    else:
        form = SignInForm()

    return render(request, "registration/signin.html", {"form": form})


def signup_view(request: HttpRequest):

    if request.method == "POST":
        form = SignUpForm(request.POST)
    else:
        form = SignUpForm()

    return render(request, "registration/signup.html", {"form": form})


def logout_view(request: HttpRequest):

    logout(request)
    redirect_url = reverse_lazy("list")

    return HttpResponseRedirect(redirect_url)
