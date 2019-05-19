from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
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
