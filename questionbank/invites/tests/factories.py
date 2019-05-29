from factory import DjangoModelFactory, Faker, SubFactory, post_generation

from questionbank.invites.models import Invite
from questionbank.users.tests.factories import UserFactory, SpecialtyFactory


class InviteFactory(DjangoModelFactory):
    username = Faker('user_name')
    email = Faker('email')
    created_by = SubFactory(UserFactory)
    specialty = SubFactory(SpecialtyFactory)

    class Meta:
        model = Invite

    @post_generation
    def role(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for role in extracted:
                self.role.add(role)

