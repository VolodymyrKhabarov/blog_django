"""
Module for defining and describing users models.
"""
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    pass
