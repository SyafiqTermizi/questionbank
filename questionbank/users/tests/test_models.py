import pytest

pytestmark = pytest.mark.django_db


def test_user_str(user):
    assert user.username == user.__str__()


def test_specialty_str(specialty):
    assert specialty.name == specialty.__str__()
