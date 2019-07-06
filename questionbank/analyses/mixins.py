from django.shortcuts import reverse

from questionbank.questions.models import Question


class AnalysisSuccessUrlMixin:

    def get_success_url(self):
        return reverse(
            'questions:detail', kwargs={'pk': self.kwargs['question_id']}
        )


class AnalysisContextDataMixin:

    def get_context_data(self):
        context = super().get_context_data()
        context['question_id'] = self.kwargs['question_id']
        return context


class AnalysisFormMixin(AnalysisSuccessUrlMixin, AnalysisContextDataMixin):

    def form_valid(self, form):
        form.instance.question = Question(pk=self.kwargs['question_id'])
        self.object = form.save()
        return super().form_valid(form)
