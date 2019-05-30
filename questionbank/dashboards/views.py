from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class Dashboard(LoginRequiredMixin, TemplateView):
    """
    Admin dashboard
    - total number of exam --> exam list
    - total number of question --> question list
    - total number of subject --> subject list
    - active invitation --> invite list

    - graph of question against subject
    - table of most used tags in question --> link to filtered question

    coordinator dashboard
    - number of exam for subject
    - number of question for subject
    - number of question created by himself
    - number of unresolved comment

    Lecturer dashboard
    - Number of question created --> question list
    - number of unresolved comment --> question list

    - list of unresolve comment --> single comment view ?
    - profile information --> profile view
      - name
      - email
      - last login
      - specialty
    """
    template_name = 'dashboards/index.html'
