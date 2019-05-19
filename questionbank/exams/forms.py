from django import forms

from .models import Exam


class ExamForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['questions'].required = False

    class Meta:
        model = Exam
        fields = ['questions']
        widgets = {
            'questions': forms.CheckboxSelectMultiple()
        }
