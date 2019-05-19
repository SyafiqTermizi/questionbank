from factory import DjangoModelFactory, Faker, SubFactory

from questionbank.subjects.tests.factories import SubjectFactory
from questionbank.users.tests.factories import UserFactory

from questionbank.exams.models import Exam


class ExamFactory(DjangoModelFactory):
    name = Faker('name')
    session = Faker('name')
    subject = SubFactory(SubjectFactory)
    created_by = SubFactory(UserFactory)

    class Meta:
        model = Exam
