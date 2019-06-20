from django import forms


class CheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    template_name = 'select_multiple.html'
