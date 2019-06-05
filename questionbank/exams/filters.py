import django_filters

from .models import Exam


class ExamFilter(django_filters.FilterSet):

    class Meta:
        model = Exam
        fields = {
            'name': ['icontains'],
            'session': ['icontains'],
            'course__code': ['iexact'],
        }
