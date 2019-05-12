from factory import DjangoModelFactory, Faker

from questionbank.invites.models import Invite


class InviteFactory(DjangoModelFactory):
    username = Faker('user_name')
    email = Faker('email')
    role = 'Admin'

    class Meta:
        model = Invite
