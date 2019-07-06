from django.shortcuts import reverse


class AnalysisSuccessUrlMixin:

    def get_success_url(self):
        return reverse(
            'question:detail', kwargs={'pk': self.kwargs['question_id']}
        )
