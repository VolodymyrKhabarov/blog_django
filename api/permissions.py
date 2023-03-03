"""
This module defines the permissions used in the API application.

"""

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthenticatedOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:
            return True

        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        if request.method in ["PUT", "PATCH", "DELETE"]:
            return obj.author == request.user

        return True
