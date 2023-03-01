"""
Users application serializers.

"""

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token

UserModel = get_user_model()


class UserModelSerializer(serializers.ModelSerializer):
    """
    Serializer for the UserModel model
    """

    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = UserModel
        fields = "id", "username", "first_name", "last_name", "email", "password", "token"

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = super().create(validated_data)
        return user

    def get_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj)
        return token.key

