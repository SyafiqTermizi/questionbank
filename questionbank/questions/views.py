from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.db.models import F
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from taggit.models import Tag
from django_filters.views import FilterView

from questionbank.subjects.models import Subject

from .filters import QuestionFilter, QuestionApiFilter
from .serializers import QuestionSerializer
from .mixins import LimitedQuestionMixin, QuestionByCourseMixin
from .forms import QuestionForm
from .models import Question


class QuestionListView(PermissionRequiredMixin, LimitedQuestionMixin, FilterView):
    permission_required = 'questions.view_question'
    model = Question
    filterset_class = QuestionFilter
    template_name_suffix = '_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        qs = self.get_queryset()

        context = super().get_context_data(**kwargs)
        context['courses'] = Subject.objects.values('name', 'code')
        context['tags'] = Tag.objects.values('name')
        context['topics'] = qs.values_list('topic', flat=True)

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
            qs = Question.objects.select_related('course')
            question = get_object_or_404(qs, pk=question_id)
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
        if user_specialties.exists():
            specialties = list(user_specialties.values_list('name', flat=True))
            question.tags.add(*specialties)

        return HttpResponseRedirect(reverse('questions:list'))


class QuestionDetailView(PermissionRequiredMixin, LimitedQuestionMixin, DetailView):
    permission_required = 'questions.view_question'
    model = Question

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unresolved_comment'] = self.object.comments.filter(
            is_resolved=False
        ).count()
        return context


class QuestionUpdateView(PermissionRequiredMixin, LimitedQuestionMixin,
                         SuccessMessageMixin, UpdateView):
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


class QuestionListApiView(QuestionByCourseMixin, ListAPIView):
    serializer_class = QuestionSerializer
    filterset_class = QuestionApiFilter


class TopicListApiView(QuestionByCourseMixin, APIView):

    def get(self, request, *args, **kwargs):
        topics = list(
            self.get_queryset().distinct().values_list('topic', flat=True)
        )
        return Response(topics)


class TagListApiView(QuestionByCourseMixin, APIView):

    def get(self, request, *args, **kwargs):
        tags = list(
            self.get_queryset().annotate(
                name=F("tags__name"), tag_id=F("tags__id")
            ).values(
                "name", "tag_id"
            )
        )
        return Response(tags)
