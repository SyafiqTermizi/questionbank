import pytest

from questionbank.exams.forms import ExamQuestionForm

pytestmark = pytest.mark.django_db


def test_exam_form_init(subject):
    """
    ExamForm questions field should not be required
    """
    with pytest.raises(KeyError):
        # ExamForm require subject as kwargs
        form = ExamQuestionForm()

    form = ExamQuestionForm(course=subject)
    assert not form.fields['questions'].required
