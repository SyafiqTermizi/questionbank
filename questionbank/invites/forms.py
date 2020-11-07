from django import forms
from django.contrib.auth import get_user_model

from .models import Invite

User = get_user_model()


class InviteForm(forms.ModelForm):

    class Meta:
        fields = ('username', 'email', 'roles', 'course', 'specialty')
        model = Invite
        widgets = {
            'roles': forms.CheckboxSelectMultiple(),
            'specialty': forms.CheckboxSelectMultiple(),
        }

    def clean_username(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username=data).exists():
            raise forms.ValidationError('Username already exist')
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already exist')
        return data
