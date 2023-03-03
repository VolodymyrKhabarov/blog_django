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
        fields = "id", "title", "body", "slug", "created_at", "updated_at", "category", "author"
        read_only_fields = ("id", "author", "slug", "created_at", "updated_at")

    def create(self, validated_data):
        category_data = validated_data.pop("category")
        try:
            category = BlogpostCategoryModel.objects.get(name=category_data["name"])
        except BlogpostCategoryModel.DoesNotExist:
            raise serializers.ValidationError("Category does not exist")
        request = self.context.get("request")
        author = request.user if request and hasattr(request, "user") else None
        blogpost = BlogpostModel.objects.create(category=category, author=author, **validated_data)
        return blogpost

    def update(self, instance, validated_data):
        category_data = validated_data.pop("category")
        try:
            category = BlogpostCategoryModel.objects.get(name=category_data["name"])
        except BlogpostCategoryModel.DoesNotExist:
            raise serializers.ValidationError("Category does not exist")
        instance.category, created = BlogpostCategoryModel.objects.update_or_create(
            name=category_data["name"], defaults=category_data
        )
        instance.title = validated_data.get("title", instance.title)
        instance.body = validated_data.get("body", instance.body)
        instance.slug = validated_data.get("slug", instance.slug)
        instance.save()
        return instance
