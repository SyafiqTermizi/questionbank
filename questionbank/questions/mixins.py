from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404

from questionbank.users.constants import COORDINATOR
from questionbank.exams.models import Exam

from .models import Question


class LimitedQuestionMixin:
    """
    limit QS to user's question if the user is not admin
    """
    def get_queryset(self):
        queryset = self.model.objects.select_related(
            'created_by', 'course', 'analysis'
        ).prefetch_related(
            'tags'
        ).order_by('-created_at')

        if self.request.user.is_superuser:
            return queryset
        elif self.request.user.role == COORDINATOR:
            return queryset.filter(course=self.request.user.course)

        # Normal User can only view question created by themselves
        return queryset.filter(created_by=self.request.user)


class QuestionByCourseMixin:
    """
    Limit query to question model by course_id that is passed by query_params
    """
    def get_queryset(self):
        exam_id = self.request.query_params.get('exam_id')

        if not exam_id:
            raise NotFound

        course = get_object_or_404(Exam, pk=exam_id).course

        return Question.objects.filter(course_id=course.pk)
