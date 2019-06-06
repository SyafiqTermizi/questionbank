import pytest
from django.shortcuts import reverse

from questionbank.users.constants import ADMIN

pytestmark = pytest.mark.django_db


def test_user_str(user):
    assert user.username == user.__str__()


def test_user_role(user, admin_user):
    """
    calling user.role method should return the user group which they are in.
    if the user is not in any group, NotImplementedError is raised
    """
    assert admin_user.role == ADMIN

    with pytest.raises(NotImplementedError):
        assert user.role


def test_specialty_str(specialty):
    assert specialty.name == specialty.__str__()


def test_specialty_get_absolute_url(specialty):
    assert specialty.get_absolute_url() == reverse(
        'users:specialty_update', kwargs={'pk': specialty.pk}
    )
