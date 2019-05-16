from factory import DjangoModelFactory, Faker

from questionbank.subjects.models import Subject


class SubjectFactory(DjangoModelFactory):
    code = Faker('email')
    name = Faker('name')

    class Meta:
        model = Subject
