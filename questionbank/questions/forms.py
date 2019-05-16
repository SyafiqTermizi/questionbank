from django import forms
from django.forms import inlineformset_factory

from .models import Question, Choice


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('question', 'subject', 'tags')


class ChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice
        exclude = ('question',)


QuestionFormSet = inlineformset_factory(
    Question, Choice, form=ChoiceForm, extra=4
)
