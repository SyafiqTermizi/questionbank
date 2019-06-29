import pytest

from django.forms import model_to_dict
from questionbank.questions.forms import QuestionForm

pytestmark = pytest.mark.django_db


def test_question_form():
    """
    QuestionForm tags field should not be required
    """
    form = QuestionForm()
    assert not form.fields['tags'].required


def test_question_form_field_order():
    """
    QuestionForm field should be in the order
    """
    form = QuestionForm()
    assert form.field_order == ['exam', 'course', 'question', 'tags']


def test_question_form_clean(question, exam):
    """
    QuestionForm should not be valid because the question and exam does not
    have the same subject
    """
    data = model_to_dict(question)
    data['exam'] = exam.pk
    form = QuestionForm(data=data)

    assert not form.is_valid()
    assert form.errors['__all__'] == ["Exam's subject and question subject must be the same"]
