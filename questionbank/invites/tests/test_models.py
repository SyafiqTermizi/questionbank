import pytest

from questionbank.users.constants import ADMIN
from questionbank.invites.models import Invite

pytestmark = pytest.mark.django_db


def test_invite_model_save(user, specialty):
    """
    calling Invite.save() should create a random token
    """
    invite = Invite.objects.create(
        username='test',
        email='test',
        created_by=user,
        specialty=specialty
    )
    # the token should exist
    assert invite.token
