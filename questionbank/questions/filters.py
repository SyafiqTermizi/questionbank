import django_filters

from .models import Question


class QuestionFilter(django_filters.FilterSet):

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
            'question': ['icontains']
        }
