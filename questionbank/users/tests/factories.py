from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from factory import DjangoModelFactory, Faker, post_generation

from questionbank.users.models import Specialty


class UserFactory(DjangoModelFactory):
    username = Faker('user_name')
    email = Faker('email')
    name = Faker('name')

    @post_generation
    def password(self, create, extracted, **kwargs):
        password = Faker(
            'password',
            length=42,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        ).generate(extra_kwargs={})
        self.set_password(password)

    class Meta:
        model = get_user_model()
        django_get_or_create = ['username']


class SpecialtyFactory(DjangoModelFactory):
    name = Faker('name')

    class Meta:
        model = Specialty


class GroupFactory(DjangoModelFactory):
    name = Faker('name')

    class Meta:
        model = Group
