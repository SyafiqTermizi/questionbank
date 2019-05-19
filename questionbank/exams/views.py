from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django_filters.views import FilterView

from .models import Exam
from .filters import ExamFilter
from .forms import ExamForm


class ExamListView(PermissionRequiredMixin, FilterView):
    permission_required = 'exams.view_exam'
    model = Exam
    filterset_class = ExamFilter
    template_name_suffix = '_list'
    paginate_by = 20


class ExamCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'exams.add_exam'
    model = Exam
    fields = ('name', 'session', 'subject')

    def get_success_url(self):
        if 'next' in self.request.POST:
            return reverse('exams:add_question', kwargs={'pk': self.object.pk})
        return reverse('exams:list')


class ExamUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'exams:change_exam'
    model = Exam
    success_url = reverse_lazy('exams:list')
    fields = ('name', 'session', 'subject')


class ExamQuestionView(PermissionRequiredMixin, UpdateView):
    permission_required = 'exams:change_exam'
    model = Exam
    template_name = 'exams/exam_question_form.html'
    form_class = ExamForm
    success_url = reverse_lazy('exams:list')
