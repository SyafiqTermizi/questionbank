from django import forms
from ckeditor.widgets import CKEditorWidget

from questionbank.questions.models import Question

from .models import Exam


class ExamForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.subject = kwargs.pop('subject')
        super().__init__(*args, **kwargs)
        self.fields['questions'].required = False
        self.fields['questions'].queryset = Question.objects.filter(
            subject=self.subject
        )

    class Meta:
        model = Exam
        fields = ['questions']
        widgets = {
            'questions': forms.CheckboxSelectMultiple()
        }


class ExamPrintForm(forms.ModelForm):

    class Meta:
        model = Exam
        fields = ['exam', 'is_published']
        widgets = {
            'exam': forms.CharField(widget=CKEditorWidget())
        }
        labels = {
            'is_published': 'Ready to publish'
        }
