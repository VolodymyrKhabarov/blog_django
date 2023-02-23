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
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = "id", "username", "email", "password", "password2"

    def validate(self, attrs):
        """
        Check that the passwords match
        """
        password = attrs.get("password")
        password2 = attrs.get("password2")

        if password != password2:
            raise serializers.ValidationError("Passwords do not match")

        return attrs

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user
