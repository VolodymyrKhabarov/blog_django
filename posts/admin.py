"""
Module that performs registration of models on the administrative site for post app
"""
from django.contrib import admin
from posts.models import BlogpostModel, BlogpostCategoryModel


@admin.register(BlogpostCategoryModel)
class BlogpostCategoryModelAdmin(admin.ModelAdmin):
    "Class for registration BlogpostCategory model"
    list_display = ["pk", "name"]


@admin.register(BlogpostModel)
class BlogpostModelAdmin(admin.ModelAdmin):
    "Class for registration BlogpostModel model"
    list_display = ["pk", "title", "category", "created_at", "updated_at"]
