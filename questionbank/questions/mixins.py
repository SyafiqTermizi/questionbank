from django.shortcuts import reverse

from questionbank.users.constants import COORDINATOR


class LimitedQuestionMixin:
    """
    limit QS to user's question if the user is not admin
    """
    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.model.objects\
                .order_by('-created_at')\
                .prefetch_related('created_by', 'tags')
        elif self.request.user.role == COORDINATOR:
            return self.model.objects.filter(
                course=self.request.user.course
            )
        return self.model.objects\
            .filter(created_by=self.request.user)\
            .order_by('-created_at').prefetch_related('created_by', 'tags')


class ChoiceFormMixin:
    """
    redirect to question detail view on success
    """
    def get_success_url(self):
        return reverse(
            'questions:detail',
            kwargs={'pk': self.kwargs['question']}
        )
