from questionbank.users.constants import COORDINATOR

from .models import Exam


class LimitedExamMixin:

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Exam.objects\
                .order_by('-created_at', 'course__code')\
                .prefetch_related('created_by', 'course')

        elif self.request.user.role == COORDINATOR:
            return Exam.objects\
                .filter(course=self.request.user.course)\
                .order_by('-created_at', 'course__code')\
                .prefetch_related('created_by', 'course')

        return Exam.objects.none()
