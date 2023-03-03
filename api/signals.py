"""
This module defines the signals used in the API application.

"""

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    Create an authentication token for the user instance after the instance is saved.
    This function is called by the `post_save` signal sent by Django's User model.
    """
    if created:
        Token.objects.create(user=instance)
