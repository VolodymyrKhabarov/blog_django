"""
API application views

"""

from rest_framework import viewsets


from posts.models import BlogpostCategoryModel, BlogpostModel
from posts.serializers import BlogpostCategoryModelSerializer, BlogpostModelSerializer
from users.models import UserModel
from users.serializers import UserModelSerializer


class BlogpostCategoryViewSet(viewsets.ModelViewSet):
    """
    API view for handling BlogpostCategoryModel objects
    """
    queryset = BlogpostCategoryModel.objects.all()
    serializer_class = BlogpostCategoryModelSerializer


class BlogpostViewSet(viewsets.ModelViewSet):
    """
    API view for handling BlogpostModel objects
    """
    queryset = BlogpostModel.objects.all()
    serializer_class = BlogpostModelSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API viewset for UserModel objects
    """
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
