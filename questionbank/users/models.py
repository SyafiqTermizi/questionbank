from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField('Full Name', max_length=255, blank=True)
    email = models.EmailField('email address', blank=False, unique=True)

    def __str__(self):
        return self.username
