from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager

from questionbank.subjects.models import Subject

User = get_user_model()


class Question(models.Model):
    question = RichTextUploadingField()
    subject = models.ForeignKey(
        Subject, on_delete=models.SET_NULL, null=True, related_name='subjects'
    )
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='questions'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = TaggableManager()


class Choice(models.Model):
    choice = RichTextUploadingField()
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='choices'
    )
