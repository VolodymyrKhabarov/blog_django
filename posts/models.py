"""
Module for defining and describing posts models.
"""
from django.db import models
from django.utils.text import slugify


class BlogpostCategoryModel(models.Model):
    "Class for defining and describing BlogpostCategoryModel model"

    class Meta:
        "Class Meta is used to provide metadata to the BlogpostCategoryModel model"

        db_table = "category"
        verbose_name = "category"
        verbose_name_plural = "categories"

    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class BlogpostModel(models.Model):
    "Class for defining and describing BlogpostMode model"

    class Meta:
        "Class Meta is used to provide metadata to the BlogpostModel model"

        db_table = "blogpost"
        verbose_name = "blogpost"
        verbose_name_plural = "blogposts"
        ordering = ('-updated_at',)

    title = models.CharField(max_length=64)
    body = models.TextField()
    slug = models.SlugField(max_length=64, blank=True, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, db_column="created")
    updated_at = models.DateTimeField(auto_now=True, db_column="updated")
    category = models.ForeignKey(BlogpostCategoryModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
