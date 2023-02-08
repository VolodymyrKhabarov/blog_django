"""
Posts application URL Configuration
"""

from django.urls import path
from posts.views import blogpost_list_view, blogpost_detail_view

urlpatterns = [
    path('', blogpost_list_view, name='list'),
    path('<slug:slug>/', blogpost_detail_view, name='detail')
]
