from django import forms

from .models import Subject


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ('code', 'name', 'description')
        help_texts = {
            'name': 'Course name will be capitalized'
        }


    def clean_name(self):
        """
        capitalize subject's name
        """
        name = self.cleaned_data['name']
        name = name.upper()
        return name
