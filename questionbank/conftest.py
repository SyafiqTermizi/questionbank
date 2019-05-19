import pytest

from questionbank.users.tests.factories import UserFactory, SpecialtyFactory
from questionbank.invites.tests.factories import InviteFactory
from questionbank.subjects.tests.factories import SubjectFactory
from questionbank.questions.tests.factories import QuestionFactory, ChoiceFactory
from questionbank.exams.tests.factories import ExamFactory


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def specialty():
    return SpecialtyFactory()


@pytest.fixture
def invite():
    return InviteFactory()


@pytest.fixture
def subject():
    return SubjectFactory()


@pytest.fixture
def question():
    return QuestionFactory()


@pytest.fixture
def choice():
    return ChoiceFactory()


@pytest.fixture
def exam():
    return ExamFactory()
