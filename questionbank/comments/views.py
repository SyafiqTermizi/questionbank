from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django_filters.views import FilterView

from questionbank.exams.models import Exam
from questionbank.questions.models import Question

from .filters import ExamCommentFilter, QuestionCommentFilter
from .models import ExamComment, QuestionComment
from .mixins import (
    ExamSuccessUrlMixin, ExamContextDataMixin,
    QuestionSuccessUrlMixin, QuestionContextDataMixin
)


class ExamCommentListView(PermissionRequiredMixin, ExamContextDataMixin, FilterView):
    permission_required = 'comments.view_examcomment'
    model = ExamComment
    filterset_class = ExamCommentFilter
    template_name_suffix = '_list'
    paginate_by = 20

    def get_queryset(self):
        return ExamComment.objects.filter(
            exam_id=self.kwargs['exam_id']
        ).order_by('-created_at').prefetch_related('created_by')


class ExamCommentCreateView(PermissionRequiredMixin, SuccessMessageMixin,
                            ExamSuccessUrlMixin, CreateView):
    permission_required = 'comments.add_examcomment'
    model = ExamComment
    fields = ('comment',)
    success_message = 'Comment created'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.exam = Exam(pk=self.kwargs['exam_id'])
        self.object = form.save()

        self.object.refresh_from_db()
        send_mail(
            subject=f'{self.request.user.username} commented on exam {self.kwargs["exam_id"]}',
            message=f'{self.object.comment} <br /> {self.object.exam.get_absolute_url()}',
            from_email='medicputraqbank@example.com',
            recipient_list=[self.object.exam.created_by.email],
        )

        return super().form_valid(form)


class ExamCommentUpdateView(PermissionRequiredMixin, SuccessMessageMixin,
                            ExamSuccessUrlMixin, UpdateView):
    permission_required = 'comments.change_examcomment'
    model = ExamComment
    fields = ('comment', 'is_resolved')
    success_message = 'Comment updated'

    def get_queryset(self):
        return ExamComment.objects.filter(
            created_by=self.request.user
        )


class ExamCommentResolveView(PermissionRequiredMixin, ExamSuccessUrlMixin,
                             UpdateView):
    permission_required = 'comments.change_examcomment'
    model = ExamComment
    fields = ('is_resolved',)

    def get_queryset(self):
        return QuestionComment.objects.filter(
            exam__created_by=self.request.user
        )

    def form_valid(self, form):
        form.instance.is_resolved = True
        self.object = form.save()

        send_mail(
            subject=f'{self.request.user.username} resolved your comment on exam {self.kwargs["exam_id"]}',
            message=f'{self.object.comment} <br /> {self.object.exam.get_absolute_url()}',
            from_email='medicputraqbank@example.com',
            recipient_list=[self.object.created_by.email],
        )

        return super().form_valid(form)


class ExamCommentDeleteView(PermissionRequiredMixin, ExamSuccessUrlMixin, DeleteView):
    permission_required = 'comments.delete_examcomment'
    model = ExamComment


class QuestionCommentListView(PermissionRequiredMixin, QuestionContextDataMixin,
                              FilterView):
    permission_required = 'comments.view_questioncomment'
    module = QuestionComment
    filterset_class = QuestionCommentFilter
    template_name_suffix = '_list'
    paginate_by = 20

    def get_queryset(self):
        return QuestionComment.objects.filter(
            question=self.kwargs['question_id']
        ).order_by('-created_at').prefetch_related('created_by')


class QuestionCommentCreateView(PermissionRequiredMixin, SuccessMessageMixin,
                                QuestionSuccessUrlMixin, CreateView):
    permission_required = 'comments.add_questioncomment'
    model = QuestionComment
    fields = ('comment',)
    success_message = 'Comment created'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.question = Question(pk=self.kwargs['question_id'])
        self.object = form.save()

        self.object.refresh_from_db()
        send_mail(
            subject=f'{self.request.user.username} commented on question {self.kwargs["question_id"]}',
            message=f'{self.object.comment} <br /> {self.object.question.get_absolute_url()}',
            from_email='medicputraqbank@example.com',
            recipient_list=[self.object.question.created_by.email],
        )

        return super().form_valid(form)


class QuestionCommentUpdateView(PermissionRequiredMixin, SuccessMessageMixin,
                                QuestionSuccessUrlMixin, UpdateView):
    permission_required = 'comments.change_questioncomment'
    model = QuestionComment
    fields = ('comment', 'is_resolved')
    success_message = 'Comment updated'

    def get_queryset(self):
        return QuestionComment.objects.filter(
            created_by=self.request.user
        )


class QuestionCommentResolveView(PermissionRequiredMixin, QuestionSuccessUrlMixin,
                                 UpdateView):
    permission_required = 'comments.change_questioncomment'
    model = QuestionComment
    fields = ('is_resolved',)

    def get_queryset(self):
        return QuestionComment.objects.filter(
            question__created_by=self.request.user
        )

    def form_valid(self, form):
        form.instance.is_resolved = True
        self.object = form.save()

        send_mail(
            subject=f'{self.request.user.username} resolved your comment on question {self.kwargs["question_id"]}',
            message=f'{self.object.comment} <br /> {self.object.question.get_absolute_url()}',
            from_email='medicputraqbank@example.com',
            recipient_list=[self.object.created_by.email],
        )

        return super().form_valid(form)


class QuestionCommentDeleteView(PermissionRequiredMixin, QuestionSuccessUrlMixin,
                                DeleteView):
    permission_required = 'comments.delete_questioncomment'
    model = QuestionComment
