from django import forms
from ckeditor.widgets import CKEditorWidget

from questionbank.questions.models import Question

from .models import Exam


class CheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    template_name = 'kambing.html'
    option_template_name = 'lembu.html'


class ExamForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.course = kwargs.pop('course')
        super().__init__(*args, **kwargs)
        self.fields['questions'].required = False
        self.fields['questions'].queryset = Question.objects.filter(
            course=self.course
        ).order_by('-created_at')

    class Meta:
        model = Exam
        fields = ['questions']
        widgets = {
            'questions': CheckboxSelectMultiple()
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
