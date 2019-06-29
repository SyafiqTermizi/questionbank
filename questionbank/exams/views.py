from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.utils.html import mark_safe
from django_filters.views import FilterView

from questionbank.users.constants import COORDINATOR

from .models import Exam
from .filters import ExamFilter
from .forms import ExamQuestionForm, ExamPrintForm, ExamForm
from .constants import ALPHABET_MAPPING
from .mixins import LimitedExamMixin


class ExamListView(PermissionRequiredMixin, LimitedExamMixin, FilterView):
    permission_required = 'exams.view_exam'
    model = Exam
    filterset_class = ExamFilter
    template_name_suffix = '_list'
    paginate_by = 20


class ExamCreateView(PermissionRequiredMixin, SuccessMessageMixin, LimitedExamMixin,
                     CreateView):
    permission_required = 'exams.add_exam'
    model = Exam
    form_class = ExamForm
    success_message = '%(name)s Created'

    def get_form_kwargs(self):
        kwarg = super().get_form_kwargs()
        if self.request.user.role == COORDINATOR:
            kwarg['coordinator'] = self.request.user
        return kwarg

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        if 'next' in self.request.POST:
            return reverse('exams:add_question', kwargs={'pk': self.object.pk})
        return reverse('exams:list')


class ExamUpdateView(PermissionRequiredMixin, SuccessMessageMixin, LimitedExamMixin,
                     UpdateView):
    permission_required = 'exams.change_exam'
    model = Exam
    success_url = reverse_lazy('exams:list')
    form_class = ExamForm
    success_message = '%(name)s Updated'

    def get_form_kwargs(self):
        kwarg = super().get_form_kwargs()
        if self.request.user.role == COORDINATOR:
            kwarg['coordinator'] = self.request.user
        return kwarg

    def get_queryset(self):
        return Exam.objects.all().prefetch_related(
            'questions',
            'questions__choices',
            'questions__comments'
        )


class ExamQuestionView(PermissionRequiredMixin, LimitedExamMixin, UpdateView):
    permission_required = 'exams.change_exam'
    model = Exam
    template_name = 'exams/exam_question_form.html'
    form_class = ExamQuestionForm
    success_url = reverse_lazy('exams:list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['course'] = self.object.course
        return kwargs


class ExamDeleteView(PermissionRequiredMixin, LimitedExamMixin, DeleteView):
    permission_required = 'exams.delete_question'
    model = Exam
    success_url = reverse_lazy('exams:list')


class ExamPrintView(PermissionRequiredMixin, LimitedExamMixin, UpdateView):
    permission_required = 'exams.add_exam'
    template_name = 'exams/create_exam.html'
    model = Exam
    form_class = ExamPrintForm
    queryset = Exam.objects.prefetch_related('questions', 'questions__choices')

    def get_initial(self):
        counter = 0
        paper = ''

        for question in self.object.questions.order_by('specialty'):
            counter += 1
            paper += (str(counter) + '. ' + question.question)

            inner_counter = 0

            for choice in question.choices.all():
                inner_counter += 1
                paper += (ALPHABET_MAPPING[inner_counter] + choice.choice)

        initial = super().get_initial()
        initial['exam'] = mark_safe(paper)
        return initial

    def get_success_url(self):
        return self.object.get_absolute_url()
