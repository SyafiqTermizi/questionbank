from django_filters import FilterSet, rest_framework as filter

from .models import Question


class QuestionFilter(FilterSet):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['tags__name__icontains'].label = 'Tags name'
        self.filters['course__name__icontains'].label = 'Course name'

    class Meta:
        model = Question
        fields = {
            'course__code': ['iexact'],
            'tags__name': ['icontains'],
            'course__name': ['icontains'],
            'question': ['icontains'],
            'topic': ['icontains']
        }


class QuestionApiFilter(filter.FilterSet):
    topic = filter.CharFilter(field_name='topic', lookup_expr='iexact')

    class Meta:
        model = Question
        fields = ['topic', 'tags__id']
