"""
Posts application serializers.

"""

from rest_framework import serializers

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

    class Meta:
        model = BlogpostModel
        fields = "id", "title", "body", "slug", "created_at", "updated_at", "category"
