import requests
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.utils.html import mark_safe
from django.shortcuts import get_object_or_404
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
    queryset = Exam.objects.prefetch_related('questions')

    def get(self, request, *args, **kwargs):
        counter = 0
        paper = ""
        self.object = get_object_or_404(Exam, pk=self.kwargs["pk"])
        for question in self.object.questions.order_by("specialty"):
            counter += 1
            choices = ""

            for c in question.get_display_choices:
                choices += c["text"]

            paper += f"""
                {question.question[:3]}
                <b>{counter}.&nbsp;</b>\
                {question.question[3:]}
                {choices}
                <br>
            """
        res = requests.post("http://storage.putraqbank.tk", json={"text": paper})
        return HttpResponseRedirect(res.json()["file"])

    def get_success_url(self):
        return self.object.get_absolute_url()
