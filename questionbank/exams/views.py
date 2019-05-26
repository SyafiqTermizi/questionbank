from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.html import mark_safe
from django_filters.views import FilterView

from .models import Exam
from .filters import ExamFilter
from .forms import ExamForm, ExamPrintForm


class ExamListView(PermissionRequiredMixin, FilterView):
    permission_required = 'exams.view_exam'
    model = Exam
    filterset_class = ExamFilter
    template_name_suffix = '_list'
    paginate_by = 20

    def get_queryset(self):
        return Exam.objects.all().prefetch_related('created_by', 'subject')


class ExamCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'exams.add_exam'
    model = Exam
    fields = ('name', 'session', 'subject')
    success_message = '%(name)s Created'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        if 'next' in self.request.POST:
            return reverse('exams:add_question', kwargs={'pk': self.object.pk})
        return reverse('exams:list')


class ExamUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'exams:change_exam'
    model = Exam
    success_url = reverse_lazy('exams:list')
    fields = ('name', 'session', 'subject')
    success_message = '%(name)s Updated'

    def get_queryset(self):
        return Exam.objects.all().prefetch_related('questions', 'questions__choices')


class ExamQuestionView(PermissionRequiredMixin, UpdateView):
    permission_required = 'exams:change_exam'
    model = Exam
    template_name = 'exams/exam_question_form.html'
    form_class = ExamForm
    success_url = reverse_lazy('exams:list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['subject'] = self.object.subject
        return kwargs


class ExamDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'exams:delete_question'
    model = Exam
    success_url = reverse_lazy('exams:list')


class ExamPrintView(PermissionRequiredMixin, FormView):
    permission_required = 'exams.add_exam'
    template_name = 'exams/create_exam.html'
    form_class = ExamPrintForm

    def get_initial(self):
        exam = get_object_or_404(
            Exam.objects.prefetch_related('questions', 'questions__choices'),
            pk=self.kwargs['pk']
        )
        paper = ''
        for question in exam.questions.all():
            paper += question.question
            for choice in question.choices.all():
                paper += choice.choice
        initial = super().get_initial()
        initial['exam'] = mark_safe(paper)
        return initial
