import pytest

from django.forms.models import model_to_dict

from questionbank.subjects.forms import SubjectForm

pytestmark = pytest.mark.django_db


def test_subject_form(subject):
    """
    the form should check if the subject code already exist
    """

    # calling the form with existing subject
    form = SubjectForm(data=model_to_dict(subject))

    # the form should not be valid because the subject already exist
    assert not form.is_valid()


def test_subject_form_clean_name(subject):
    """
    Subject name should be capitalized by clean_name() method
    """
    form = SubjectForm(
        data={
            'code': 'SKM123',
            'name': 'aaa'
        }
    )
    assert form.is_valid()
    assert form.cleaned_data['name'].isupper()
