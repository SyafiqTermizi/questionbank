from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.db.models.functions import Length
from django_filters.views import FilterView
from taggit.models import Tag

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
        context['tags'] = Tag.objects.all()
        topics = Question.objects.annotate(tpc=Length('topic'))\
                            .filter(tpc__gt=1)\
                            .values_list('topic', flat=True)
        context['topics'] = set(topics)
        return context


class QuestionCreateView(PermissionRequiredMixin, SuccessMessageMixin,
                         LimitedQuestionMixin, CreateView):
    permission_required = 'questions.add_question'
    model = Question
    form_class = QuestionForm
    success_message = 'Question Created !'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        question_id = self.request.GET.get('question', 0)

        if question_id:
            question = get_object_or_404(Question, pk=question_id)
            kwargs['initial'] = {
                'question': question.question,
                'tags': question.tags.all(),
                'course': question.course,
                'choices': question.choices
            }
        return kwargs

    def form_valid(self, form):
        question = form.save(commit=False)
        question.created_by = self.request.user
        question.save()
        form.save_m2m()

        # handling cases where user don't have specialty
        # e.g admin users
        user_specialties = self.request.user.specialty
        if user_specialties.count():
            specialties = list(user_specialties.values_list('name', flat=True))
            question.tags.add(*specialties)

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

    def get_success_url(self):
        return self.request.GET.get("next") or super().get_success_url()


class QuestionDeleteView(PermissionRequiredMixin, LimitedQuestionMixin, DeleteView):
    permission_required = 'questions.delete_question'
    model = Question
    success_url = reverse_lazy('questions:list')
