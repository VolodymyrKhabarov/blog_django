from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout

from users.models import UserModel


# def signin_view(request: HttpRequest) -> HttpResponse:
#     return render(request, "registration/signin.html")

def signin_view(request: HttpRequest):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            redirect_url = reverse_lazy("list")

            return HttpResponseRedirect(redirect_url)

        return render(request, "registration/signin.html")

    return render(request, "registration/signin.html")


# def signup_view(request: HttpRequest) -> HttpResponse:
#     return render(request, "registration/signup.html")

def signup_view(request: HttpRequest):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            return render(request, "registration/signup.html")

        try:
            UserModel.objects.get(username=username)
            return render(request, "registration/signup.html")
        except UserModel.DoesNotExist:
            UserModel.objects.create_user(username=username, email=email, password=password)

        redirect_url = reverse_lazy("signin")

        return HttpResponseRedirect(redirect_url)

    return render(request, "registration/signup.html")


def logout_view(request: HttpRequest):

    logout(request)
    redirect_url = reverse_lazy("list")

    return HttpResponseRedirect(redirect_url)