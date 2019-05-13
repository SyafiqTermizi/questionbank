from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .models import Question


class QuestionListView(PermissionRequiredMixin, ListView):
    permission_required = 'questions.view_question'
    model = Question
    paginate_by = 10


class QuestionCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'questions.add_question'
    model = Question
    fields = ('subject', 'question')
    success_url = reverse_lazy('questions:list')
    success_message = 'Question Created !'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        self.object = form.save()
        return super().form_valid(form)


class QuestionUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'questions.change_question'
    model = Question
    fields = ('subject', 'question')
    success_url = reverse_lazy('questions:list')
    success_message = 'Question Updated !'


class QuestionDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'questions.delete_question'
    model = Question
    success_url = reverse_lazy('questions:list')
