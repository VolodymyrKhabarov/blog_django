"""
Module for defining and describing users models.
"""
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):

    class Meta:
        db_table = "user"
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ["username"]

    def __str__(self):
        return self.username
