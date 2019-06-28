import pytest

from questionbank.questions.forms import QuestionForm

pytestmark = pytest.mark.django_db


def test_question_form():
    """
    QuestionForm tags field should not be required
    """
    form = QuestionForm()
    assert not form.fields['tags'].required
