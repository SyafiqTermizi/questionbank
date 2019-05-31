from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from ckeditor_uploader.fields import RichTextUploadingField

from questionbank.questions.models import Question
from questionbank.subjects.models import Subject

User = get_user_model()


class Exam(models.Model):
    name = models.CharField(max_length=250)
    session = models.CharField(max_length=255)
    is_published = models.BooleanField(default=False)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    exam = RichTextUploadingField(blank=True)  # the exam question and choices
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='exams'
    )
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('exams:update', kwargs={'pk': self.pk})
