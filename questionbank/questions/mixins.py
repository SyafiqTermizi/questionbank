from django.shortcuts import reverse


class ChoiceFormMixin:

    def get_success_url(self):
        return reverse(
            'questions:detail',
            kwargs={'pk': self.kwargs['question']}
        )
