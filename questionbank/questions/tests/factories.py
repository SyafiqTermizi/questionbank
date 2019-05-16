from factory import DjangoModelFactory, Faker, SubFactory

from questionbank.users.tests.factories import UserFactory
from questionbank.subjects.tests.factories import SubjectFactory
from questionbank.questions.models import Question, Choice


class QuestionFactory(DjangoModelFactory):
    question = Faker('paragraph')
    subject = SubFactory(SubjectFactory)
    created_by = SubFactory(UserFactory)

    class Meta:
        model = Question


class ChoiceFactory(DjangoModelFactory):
    choice = Faker('paragraph')
    question = SubFactory(QuestionFactory)

    class Meta:
        model = Choice
