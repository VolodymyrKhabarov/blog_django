"""
API application URL Configuration
"""

from django.urls import include, path
from rest_framework import routers
from api.views import BlogpostCategoryViewSet, BlogpostViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'post-categories', BlogpostCategoryViewSet)
router.register(r'posts', BlogpostViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
