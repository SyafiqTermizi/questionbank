from django import forms
from django.forms import inlineformset_factory

from questionbank.exams.models import Exam

from .models import Question, Choice


class QuestionForm(forms.ModelForm):
    exam = forms.ModelChoiceField(
        queryset=Exam.objects.order_by('-created_at'), required=False
    )
    field_order = ['exam', 'course', 'question', 'tags']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].required = False

        if kwargs.get('instance', None):
            self.fields['exam'].initial = kwargs['instance'].exam.first().pk

    class Meta:
        model = Question
        fields = ('course', 'question', 'tags')

    def save(self):
        instance = super().save()
        instance.exam.clear()
        if self.cleaned_data['exam']:
            instance.exam.add(self.cleaned_data['exam'])
        return instance


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
