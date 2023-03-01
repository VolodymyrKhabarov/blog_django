"""
API application views

"""

from rest_framework import viewsets
from rest_framework.response import Response

from api.permissions import IsAuthenticatedOrReadOnly
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
    permission_classes = [IsAuthenticatedOrReadOnly]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    """
    API viewset for UserModel objects
    """
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

