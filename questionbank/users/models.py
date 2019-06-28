from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from questionbank.subjects.models import Subject

from .constants import ADMIN, COORDINATOR, LECTURER


class Specialty(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'specialties'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('users:specialty_update', kwargs={'pk': self.pk})


class User(AbstractUser):
    name = models.CharField('Full Name', max_length=255, blank=True)
    email = models.EmailField('email address', blank=False, unique=True)
    specialty = models.ForeignKey(Specialty, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(
        Subject,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username

    @property
    def role(self):
        """
        Return user groups. If the user have two group, it returns,
        the one with highest priority
        """
        roles = list(self.groups.values_list('name', flat=True))
        if ADMIN in roles or self.is_superuser:
            return ADMIN
        elif COORDINATOR in roles:
            return COORDINATOR
        elif LECTURER in roles:
            return LECTURER
        raise NotImplementedError
