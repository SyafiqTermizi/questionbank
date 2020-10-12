from django import forms
from django.forms import inlineformset_factory

from .models import Question


class QuestionForm(forms.ModelForm):
    field_order = ['course', 'question', 'tags']

    class Meta:
        model = Question
        fields = ('course', 'question', 'tags', 'choices')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].required = False
