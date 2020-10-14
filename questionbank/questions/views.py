from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django_filters.views import FilterView

from questionbank.subjects.models import Subject

from .mixins import LimitedQuestionMixin
from .filters import QuestionFilter
from .models import Question
from .forms import QuestionForm


class QuestionListView(PermissionRequiredMixin, LimitedQuestionMixin, FilterView):
    permission_required = 'questions.view_question'
    filterset_class = QuestionFilter
    template_name_suffix = '_list'
    paginate_by = 10
    model = Question
    querset = Question.objects.prefetch_related('exam')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Subject.objects.all()
        return context


class QuestionCreateView(PermissionRequiredMixin, SuccessMessageMixin,
                         LimitedQuestionMixin, CreateView):
    permission_required = 'questions.add_question'
    model = Question
    form_class = QuestionForm
    success_message = 'Question Created !'

    def form_valid(self, form):
        question = form.save(commit=False)
        question.created_by = self.request.user
        question.save()        
        return HttpResponseRedirect(reverse('questions:list'))


class QuestionDetailView(PermissionRequiredMixin, LimitedQuestionMixin, DetailView):
    permission_required = 'questions.view_question'
    model = Question

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unresolved_comment'] = self.object.comments.filter(is_resolved=False).count()
        return context


class QuestionUpdateView(PermissionRequiredMixin, SuccessMessageMixin,
                         LimitedQuestionMixin, UpdateView):
    permission_required = 'questions.change_question'
    model = Question
    form_class = QuestionForm
    success_url = reverse_lazy('questions:list')
    success_message = 'Question Updated !'


class QuestionDeleteView(PermissionRequiredMixin, LimitedQuestionMixin, DeleteView):
    permission_required = 'questions.delete_question'
    model = Question
    success_url = reverse_lazy('questions:list')
