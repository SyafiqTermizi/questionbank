from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model

from questionbank.users.constants import CHOICES
from questionbank.users.models import Specialty

User = get_user_model()


class Invite(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    token = models.CharField(max_length=30, blank=True, unique=True)
    role = models.CharField(max_length=20, choices=CHOICES)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.token = get_random_string(length=30)
        super().save(*args, **kwargs)
