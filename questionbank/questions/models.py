import json
from operator import itemgetter

from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.utils.html import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager

from questionbank.exams.constants import ALPHABET_MAPPING
from questionbank.subjects.models import Subject
from questionbank.users.models import Specialty

User = get_user_model()


class Question(models.Model):
    question = RichTextUploadingField()

    # A JSON field store the question choices.
    # The content will look like
    # [{
    #   choice: '<html></html>',
    #   is_correct: False,
    #  }]
    choices = models.JSONField()
    topic = models.CharField(max_length=255, blank=True)

    course = models.ForeignKey(
        Subject, on_delete=models.SET_NULL, null=True, related_name='subjects'
    )
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='questions'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    specialty = models.ForeignKey(
        to=Specialty, on_delete=models.SET_NULL, null=True, blank=True
    )
    tags = TaggableManager()

    class Meta:
        ordering = ['specialty']

    def __str__(self):
        full_questions = f"{self.question} <br> {self.get_display_choices}"
        return mark_safe(full_questions)

    def get_absolute_url(self):
        return reverse('questions:detail', kwargs={'pk': self.pk})

    @property
    def unresolve_comment(self):
        return self.comments.filter(is_resolved=False).count()

    @property
    def get_display_choices(self):
        choices = ""
        sorted_choices = sorted(self.choices, key=itemgetter("text"), reverse=False)

        for index in range(len(sorted_choices)):
            text = f'\
                {sorted_choices[index]["text"][:3]}\
                <b>{ALPHABET_MAPPING[index+1]})&nbsp;</b>\
                {sorted_choices[index]["text"][3:]}'
            choices += text
        return choices

    def display_schema_choices(self):
        choices = ""
        sorted_choices = sorted(self.choices, key=itemgetter("text"), reverse=False)

        for index in range(len(sorted_choices)):
            text = f'\
                {sorted_choices[index]["text"][:3]}\
                <b>{ALPHABET_MAPPING[index+1]})&nbsp;</b>\
                {sorted_choices[index]["text"][3:-5]}\
                <b>&nbsp;{"(correct answer)" if sorted_choices[index]["isCorrect"] else ""}</b>\
                </p>'
            choices += text
        return choices

    @property
    def get_json_choices(self):
        return mark_safe(json.dumps(self.choices))
