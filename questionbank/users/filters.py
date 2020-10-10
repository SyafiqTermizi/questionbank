import django_filters
from django.db.models import Q

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from questionbank.users.models import Specialty

User = get_user_model()


class UserFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method='filter_username_and_email',
        label='',
    )
    specialty = django_filters.ModelChoiceFilter(
        queryset=Specialty.objects.order_by('name')
    )
    groups = django_filters.ModelChoiceFilter(
        queryset=Group.objects.order_by('name'),
        label='Role'
    )

    def filter_username_and_email(self, queryset, name, value):
        return User.objects.filter(
            Q(username__icontains=value) | Q(email__icontains=value)
        )

    class Meta:
        model = User
        fields = ['q']


class SpecialtyFilter(django_filters.FilterSet):

    class Meta:
        model = Specialty
        fields = {
            'name': ['icontains']
        }
