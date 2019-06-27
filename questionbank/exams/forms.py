from django import forms
from ckeditor.widgets import CKEditorWidget

from questionbank.questions.models import Question
from questionbank.subjects.models import Subject

from .models import Exam
from .widgets import CheckboxSelectMultiple


class ExamForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        coordninator = kwargs.pop('coordinator', None)

        super().__init__(*args, **kwargs)

        if coordninator:
            self.fields['course'].queryset = Subject.objects.filter(name=coordninator.course.name)

    class Meta:
        model = Exam
        fields = ['name', 'session', 'course']


class ExamQuestionForm(forms.ModelForm):

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
