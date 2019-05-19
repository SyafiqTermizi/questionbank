import pytest

# from questionbank.exams.models import Exam

pytestmark = pytest.mark.django_db


def test_exam_model_str(exam):
    """
    calling exam.__str__() should return exam.name
    """
    assert exam.name == exam.__str__()
