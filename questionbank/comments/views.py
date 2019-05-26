from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import reverse
from django_filters.views import FilterView

from questionbank.exams.models import Exam
from questionbank.questions.models import Question

from .filters import ExamCommentFilter, QuestionCommentFilter
from .models import ExamComment, QuestionComment
from .mixins import ExamSuccessUrlMixin, QuestionSuccessUrlMixin, QuestionContextDataMixin


class ExamCommentListView(PermissionRequiredMixin, FilterView):
    permission_required = 'comments.view_examcomment'
    model = ExamComment
    filterset_class = ExamCommentFilter
    template_name_suffix = '_list'
    paginate_by = 20

    def get_queryset(self):
        return ExamComment.objects.filter(
            exam_id=self.kwargs['exam_id']
        )


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
        return super().form_valid(form)


class ExamCommentUpdateView(PermissionRequiredMixin, SuccessMessageMixin,
                            ExamSuccessUrlMixin, UpdateView):
    permission_required = 'comments.change_examcomment'
    model = ExamComment
    fields = ('comment', 'is_resolved')
    success_message = 'Comment updated'


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
        ).prefetch_related('created_by')


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
        return super().form_valid(form)


class QuestionCommentUpdateView(PermissionRequiredMixin, SuccessMessageMixin,
                                QuestionSuccessUrlMixin, UpdateView):
    permission_required = 'comments.change_questioncomment'
    model = QuestionComment
    fields = ('comment', 'is_resolved')
    success_message = 'Comment updated'


class QuestionCommentResolveView(PermissionRequiredMixin, QuestionSuccessUrlMixin, UpdateView):
    permission_required = 'comments.change_questioncomment'
    model = QuestionComment
    fields = ('is_resolved',)

    def form_valid(self, form):
        form.instance.is_resolved = True
        self.object = form.save()
        return super().form_valid(form)


class QuestionCommentDeleteView(PermissionRequiredMixin, QuestionSuccessUrlMixin,
                                DeleteView):
    permission_required = 'comments.delete_questioncomment'
    model = QuestionComment
