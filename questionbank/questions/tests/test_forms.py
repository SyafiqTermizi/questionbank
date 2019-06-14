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


def test_question_form_exam_field(question, exam):
    """
    QuestionForm should be able to save add exam instance on question
    """
    # question should not have any exam yet
    assert not question.exam.first()

    data = model_to_dict(question)
    data['exam'] = exam.pk
    form = QuestionForm(
        data=data
    )

    assert form.is_valid()
    instance = form.save()

    # question should have exam instance
    assert instance.exam.first().pk
