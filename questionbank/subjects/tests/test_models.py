import pytest

pytestmark = pytest.mark.django_db


def test_subject_model_str(subject):
    """
    calling Subject.__str__() should return subject's name
    """
    assert subject.__str__() == subject.name
