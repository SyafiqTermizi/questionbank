from django.db import models
from django.contrib.auth import get_user_model

from questionbank.questions.models import Question
from questionbank.exams.models import Exam

User = get_user_model()


class BaseComment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_resolved = models.BooleanField(default=False, verbose_name='resolved')

    class Meta:
        abstract = True


class QuestionComment(BaseComment):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE,
        related_name='comments'
    )


class ExamComment(BaseComment):
    exam = models.ForeignKey(
        Exam, on_delete=models.CASCADE,
        related_name='comments'
    )
