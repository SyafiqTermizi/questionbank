import pytest

from questionbank.users.tests.factories import UserFactory
from questionbank.invites.tests.factories import InviteFactory


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def invite():
    return InviteFactory()
