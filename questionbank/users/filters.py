import django_filters

from django.contrib.auth import get_user_model

from .models import Specialty

User = get_user_model()


class UserFilter(django_filters.FilterSet):
    specialty = django_filters.ModelChoiceFilter(
        queryset=Specialty.objects.all().order_by('name')
    )

    class Meta:
        model = User
        fields = {
            'username': ['icontains'],
            'email': ['icontains']
        }
