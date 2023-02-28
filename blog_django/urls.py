"""blog_django URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', views.obtain_auth_token, name='api-auth'),
    path('', include('users.urls')),
    path('', include('posts.urls')),
    path('', include('api.urls')),
]
