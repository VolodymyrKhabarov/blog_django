"""
Module with post application settings
"""
from django.apps import AppConfig


class PostsConfig(AppConfig):
    "Class with post app settings"
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
