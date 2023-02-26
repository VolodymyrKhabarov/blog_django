"""
Posts application serializers.

"""

from django.core.validators import MinLengthValidator
from django.utils.text import slugify
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from posts.models import BlogpostCategoryModel, BlogpostModel


class BlogpostCategoryModelSerializer(serializers.ModelSerializer):
    """
    Serializer for the BlogpostCategoryModel model
    """

    class Meta:
        model = BlogpostCategoryModel
        fields = "id", "name"


class BlogpostModelSerializer(serializers.ModelSerializer):
    """
    Serializer for the BlogpostModel model
    """
    category = BlogpostCategoryModelSerializer()
    slug = serializers.SlugField(max_length=64, validators=[
            UniqueValidator(queryset=BlogpostModel.objects.all()),
            MinLengthValidator(1)
        ])

    class Meta:
        model = BlogpostModel
        fields = "id", "title", "body", "slug", "created_at", "updated_at", "category"

    def validate(self, data):
        if "title" in data and "slug" in data:
            if slugify(data["title"]) != data["slug"]:
                raise serializers.ValidationError("Slug does not match the title")
        return data

    def create(self, validated_data):
        category_data = validated_data.pop("category")
        try:
            category = BlogpostCategoryModel.objects.get(name=category_data["name"])
        except BlogpostCategoryModel.DoesNotExist:
            raise serializers.ValidationError("Category does not exist")
        blogpost = BlogpostModel.objects.create(category=category, **validated_data)
        return blogpost
