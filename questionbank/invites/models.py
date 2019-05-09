from django.db import models
from django.utils.crypto import get_random_string


class Invite(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    token = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.token = get_random_string(length=30)
        super().save(*args, **kwargs)
