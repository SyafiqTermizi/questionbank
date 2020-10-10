import django_filters
from django.db.models import Q

from .models import Subject


class SubjectFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method='filter_code_and_name',
        label='',
    )

    class Meta:
        model = Subject
        fields = ['q']

    def filter_code_and_name(self, queryset, name, value):
        return Subject.objects.filter(
            Q(code__icontains=value) | Q(name__icontains=value)
        )
