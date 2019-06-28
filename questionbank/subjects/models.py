from django.db import models


class Subject(models.Model):
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'
        ordering = ['code']

    def __str__(self):
        return self.name
