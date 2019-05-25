import django_filters

from .models import QuestionComment, ExamComment


class QuestionCommentFilter(django_filters.FilterSet):
    is_resolved = django_filters.BooleanFilter()

    class Meta:
        model = QuestionComment
        fields = ('is_resolved',)


class ExamCommentFilter(django_filters.FilterSet):
    is_resolved = django_filters.BooleanFilter()

    class Meta:
        model = ExamComment
        fields = ('is_resolved',)
