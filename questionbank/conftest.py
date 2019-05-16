import pytest

from questionbank.users.tests.factories import UserFactory
from questionbank.invites.tests.factories import InviteFactory
from questionbank.subjects.tests.factories import SubjectFactory


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def invite():
    return InviteFactory()


@pytest.fixture
def subject():
    return SubjectFactory()
