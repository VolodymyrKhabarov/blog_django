from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render
from posts.models import BlogpostModel, BlogpostCategoryModel


def blogpost_list_view(request: HttpRequest) -> HttpResponse:
    ctx = {
        "object_list": BlogpostModel.objects.all(),
        "category_list": BlogpostCategoryModel.objects.all(),
    }
    return render(request, "homepage.html", ctx)


def blogpost_detail_view(request: HttpRequest, slug: str) -> HttpResponse:
    try:
        post = BlogpostModel.objects.get(slug=slug)
    except BlogpostModel.DoesNotExist:
        raise Http404("object not found")
    ctx = {
        "object": post,
        "category_list": BlogpostCategoryModel.objects.all(),
    }
    return render(request, "blogpost.html", ctx)
