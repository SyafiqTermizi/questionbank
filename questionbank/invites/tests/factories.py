from factory import DjangoModelFactory, Faker, SubFactory

from questionbank.invites.models import Invite
from questionbank.users.tests.factories import UserFactory, SpecialtyFactory


class InviteFactory(DjangoModelFactory):
    username = Faker('user_name')
    email = Faker('email')
    role = 'Admin'
    created_by = SubFactory(UserFactory)
    specialty = SubFactory(SpecialtyFactory)

    class Meta:
        model = Invite
