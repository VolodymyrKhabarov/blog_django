from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import login, logout

from users.forms import SignInForm, SignUpForm


def signin_view(request: HttpRequest):

    if request.method == "POST":
        form = SignInForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            redirect_url = reverse_lazy("list")

            return HttpResponseRedirect(redirect_url)

    if request.method == "GET":
        form = SignInForm()

    return render(request, "registration/signin.html", {"form": form})


def signup_view(request: HttpRequest):

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            redirect_url = reverse_lazy("signin")

            return HttpResponseRedirect(redirect_url)

    if request.method == "GET":
        form = SignUpForm()
        
    return render(request, "registration/signup.html", {"form": form})


def logout_view(request: HttpRequest):

    logout(request)
    redirect_url = reverse_lazy("list")

    return HttpResponseRedirect(redirect_url)
