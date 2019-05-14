from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django_filters.views import FilterView

from questionbank.subjects.models import Subject

from .filters import QuestionFilter
from .models import Question


class QuestionListView(PermissionRequiredMixin, FilterView):
    permission_required = 'questions.view_question'
    filterset_class = QuestionFilter
    template_name_suffix = '_list'
    paginate_by = 10
    queryset = Question.objects.all().prefetch_related('tags', 'created_by')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = Subject.objects.all()
        return context


class QuestionCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'questions.add_question'
    model = Question
    fields = ('subject', 'question', 'tags')
    success_url = reverse_lazy('questions:list')
    success_message = 'Question Created !'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        self.object = form.save()
        return super().form_valid(form)


class QuestionUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'questions.change_question'
    model = Question
    fields = ('subject', 'question', 'tags')
    success_url = reverse_lazy('questions:list')
    success_message = 'Question Updated !'


class QuestionDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'questions.delete_question'
    model = Question
    success_url = reverse_lazy('questions:list')
