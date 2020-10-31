from django import forms
from django.forms import inlineformset_factory

from .models import Question


class QuestionForm(forms.ModelForm):
    field_order = ['course', 'topic', 'question', 'tags']

    class Meta:
        model = Question
        fields = ('course', 'topic', 'question', 'tags', 'choices')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].required = False
