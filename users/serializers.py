"""
Users application serializers.

"""

from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()


class UserModelSerializer(serializers.ModelSerializer):
    """
    Serializer for the UserModel model
    """

    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = "id", "username", "email", "password"
