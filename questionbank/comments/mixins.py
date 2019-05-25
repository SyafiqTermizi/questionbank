from django.shortcuts import reverse


class ExamSuccessUrlMixin:

    def get_success_url(self):
        return reverse(
            'comments:exam_list', kwargs={'exam_id': self.kwargs['exam_id']}
        )


class QuestionSuccessUrlMixin:

    def get_success_url(self):
        return reverse(
            'comments:question_list',
            kwargs={'question_id': self.kwargs['question_id']}
        )
