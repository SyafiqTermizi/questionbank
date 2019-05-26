from django.shortcuts import reverse

from .models import ExamComment


class ExamContextDataMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exam_id'] = self.kwargs['exam_id']
        return context


class ExamSuccessUrlMixin(ExamContextDataMixin):

    def get_success_url(self):
        return reverse(
            'comments:exam_list', kwargs={'exam_id': self.kwargs['exam_id']}
        ) + '?is_resolved=false'


class QuestionContextDataMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question_id'] = self.kwargs['question_id']
        return context


class QuestionSuccessUrlMixin(QuestionContextDataMixin):

    def get_success_url(self):
        return reverse(
            'comments:question_list',
            kwargs={'question_id': self.kwargs['question_id']}
        ) + '?is_resolved=false'
