from django.shortcuts import reverse
import pytest

# from questionbank.exams.models import Exam

pytestmark = pytest.mark.django_db


def test_exam_model_str(exam):
    """
    calling exam.__str__() should return exam.name
    """
    assert exam.name == exam.__str__()


def test_exam_get_absolute_url(exam):
    """
    calling exam.get_absolute_url() should return url to exam update view
    """
    assert exam.get_absolute_url() == reverse('exams:update', kwargs={'pk': exam.pk})
