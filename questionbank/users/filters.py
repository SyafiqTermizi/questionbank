import django_filters

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from questionbank.users.models import Specialty

User = get_user_model()


class UserFilter(django_filters.FilterSet):
    specialty = django_filters.ModelChoiceFilter(
        queryset=Specialty.objects.order_by('name')
    )
    groups = django_filters.ModelChoiceFilter(
        queryset=Group.objects.order_by('name'),
        label='Role'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['username__icontains'].label = 'Username'
        self.filters['email__icontains'].label = 'Email'

    class Meta:
        model = User
        fields = {
            'username': ['icontains'],
            'email': ['icontains']
        }


class SpecialtyFilter(django_filters.FilterSet):

    class Meta:
        model = Specialty
        fields = {
            'name': ['icontains']
        }
