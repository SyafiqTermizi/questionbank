from django import forms
from django.forms import inlineformset_factory

from .models import Question, Choice


class QuestionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].required = False

    class Meta:
        model = Question
        fields = ('course', 'question', 'tags')


class ChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice
        exclude = ('question',)
        labels = {
            'is_correct': 'Correct choice'
        }


QuestionFormSet = inlineformset_factory(
    Question, Choice, form=ChoiceForm, extra=4, can_delete=False
)
