from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from questionbank.users.constants import ADMIN, COORDINATOR, LECTURER
from questionbank.exams.models import Exam
from questionbank.questions.models import Question
from questionbank.subjects.models import Subject
from questionbank.invites.models import Invite
from questionbank.comments.models import QuestionComment


class Dashboard(LoginRequiredMixin, TemplateView):
    """
    Admin dashboard
    - graph of question against subject
    - table of most used tags in question --> link to filtered question

    coordinator dashboard

    Lecturer dashboard
    - list of unresolve comment --> single comment view ?
    - profile information --> profile view
      - name
      - email
      - last login
      - specialty
    """
    template_name = 'dashboards/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # https://docs.djangoproject.com/en/2.1/ref/models/querysets/#when-querysets-are-evaluated
        role = self.request.user.role

        if role == ADMIN:
            return self.get_admin_context(context)
        elif role == COORDINATOR:
            return self.get_coordinator_context(
                context,
                course_id=self.request.user.course.pk,
                user_id=self.request.user.pk
            )
        elif role == LECTURER:
            return self.get_lecturer_context(
                context,
                user_id=self.request.user.pk
            )

    def get_admin_context(self, context={}):
        context['total_exam'] = Exam.objects.count()
        context['total_question'] = Question.objects.count()
        context['total_subject'] = Subject.objects.count()
        context['total_invites'] = Invite.objects.count()
        context['role'] = ADMIN
        return context

    def get_coordinator_context(self, context={}, course_id=0, user_id=0):
        context['total_exam'] = Exam.objects.filter(course__id=course_id).count()
        context['total_question'] = Question.objects.filter(course__id=course_id).count()
        context['total_question_created'] = Question.objects.filter(created_by__id=user_id).count()
        context['role'] = COORDINATOR
        return context

    def get_lecturer_context(self, context={}, user_id=0):
        context['total_question_created'] = Question.objects.filter(created_by__id=user_id).count()
        qs = list(Question.objects.filter(created_by__id=user_id))
        context['total_unresolved_comment'] = QuestionComment.objects.filter(question__in=qs, is_resolved=False).count()
        context['role'] = LECTURER
        return context
