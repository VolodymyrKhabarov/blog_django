"""
Module for defining and describing users models.
"""
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):

    class Meta:
        "Class Meta is used to provide metadata to the UserModel model"

        db_table = "users"
