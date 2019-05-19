from django.db import models
from django.contrib.auth import get_user_model

from questionbank.questions.models import Question
from questionbank.subjects.models import Subject

User = get_user_model()


class Exam(models.Model):
    name = models.CharField(max_length=250)
    session = models.CharField(max_length=255)
    is_published = models.BooleanField(default=False)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.name
