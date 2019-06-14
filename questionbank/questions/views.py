from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django_filters.views import FilterView

from questionbank.subjects.models import Subject

from .mixins import ChoiceFormMixin, LimitedQuestionMixin
from .filters import QuestionFilter
from .models import Question, Choice
from .forms import QuestionFormSet, QuestionForm


class QuestionListView(PermissionRequiredMixin, LimitedQuestionMixin, FilterView):
    permission_required = 'questions.view_question'
    filterset_class = QuestionFilter
    template_name_suffix = '_list'
    paginate_by = 10
    model = Question

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Subject.objects.all()
        return context


class QuestionCreateView(PermissionRequiredMixin, SuccessMessageMixin,
                         LimitedQuestionMixin, CreateView):
    permission_required = 'questions.add_question'
    model = Question
    form_class = QuestionForm
    success_url = reverse_lazy('questions:list')
    success_message = 'Question Created !'
    choice_initial = []

    def get_initial(self):
        question_id = self.request.GET.get('question', None)

        if question_id:
            # check if the query param exist && valid
            try:
                obj = get_object_or_404(Question, pk=question_id)
            except ValueError:
                raise Http404

            initial = {
                'course': obj.course,
                'question': obj.question,
                'tags': obj.tags.all()
            }

            self.choice_initial = list(
                obj.choices.values('choice', 'is_correct')
            )
            return initial
        return super().get_initial()

    def get_context_data(self):
        context = super().get_context_data()
        context['choices'] = QuestionFormSet(initial=self.choice_initial)
        return context

    def post(self, request, *args, **kwargs):
        choices = QuestionFormSet(self.request.POST, self.request.FILES)
        question = self.form_class(self.request.POST, self.request.FILES)
        if choices.is_valid():
            if question.is_valid():
                return self.form_valid(question=question, choices=choices)
        return super(QuestionCreateView, self).post(self.request)

    def form_valid(self, question, choices):
        question.instance.created_by = self.request.user
        q = question.save()

        if self.request.user.specialty:
            question.instance.tags.add(self.request.user.specialty.name)

        for choice in choices:
            if choice['choice'].value():
                choice.instance.question = q
                choice.save()
        return HttpResponseRedirect(reverse("questions:list"))


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


class ChoiceCreateView(PermissionRequiredMixin, SuccessMessageMixin, ChoiceFormMixin, CreateView):
    permission_required = 'questions.add_choice'
    model = Choice
    fields = ('choice', 'is_correct')
    success_message = 'Choice created !'

    def form_valid(self, form):
        form.instance.question = Question(pk=self.kwargs['question'])
        form.save()
        return super().form_valid(form)


class ChoiceUpdateView(PermissionRequiredMixin, SuccessMessageMixin, ChoiceFormMixin, UpdateView):
    permission_required = 'questions.change_choice'
    model = Choice
    fields = ('choice', 'is_correct')
    success_message = 'Choice Updated !'


class ChoiceDeleteView(PermissionRequiredMixin, ChoiceFormMixin, DeleteView):
    permission_required = 'questions.delete_choice'
    model = Choice
