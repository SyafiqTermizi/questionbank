import pytest

from questionbank.users.constants import ADMIN

from questionbank.invites.forms import InviteForm

pytestmark = pytest.mark.django_db


def test_invite_form_invalid(user, group):
    # Initializing form with user that already exist
    form = InviteForm(data={
        'username': user.username,
        'email': user.email,
        'role': [group]
    })

    # form should not be valid because the user already exist
    assert not form.is_valid()

    # form should contains username && email error
    assert form.errors['username'] == ['Username already exist']
    assert form.errors['email'] == ['Email already exist']


def test_invite_form_valid(user, specialty, group):
    # Initializing form with user that don't exist
    form = InviteForm(data={
        'username': 'test',
        'email': 'test@test.com',
        'role': [group],
        'specialty': specialty.id
    })

    # form should be valid because the user don't exist yet
    assert form.is_valid()

    # form should not contains any error
    assert not form.errors
