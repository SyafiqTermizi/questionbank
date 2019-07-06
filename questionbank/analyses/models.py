from django.db import models

from questionbank.questions.models import Question


class Analysis(models.Model):
    passing_index = models.DecimalField(
        verbose_name='Passing Index (PI)',
        max_digits=2,
        decimal_places=2
    )
    discrimination_index = models.DecimalField(
        verbose_name='Discrimination Index (DI)',
        max_digits=2,
        decimal_places=2
    )
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
