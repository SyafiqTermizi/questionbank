from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from .mixins import AnalysisSuccessUrlMixin
from .models import Analysis


class AnalysisCreateView(PermissionRequiredMixin, SuccessMessageMixin,
                         AnalysisSuccessUrlMixin, CreateView):
    permission_required = 'analyses.add_analysis'
    model = Analysis
    success_message = 'Analysis Created'


class AnalysisUpdateView(PermissionRequiredMixin, SuccessMessageMixin,
                         AnalysisSuccessUrlMixin, UpdateView):
    permission_required = 'analyses.delete_analysis'
    model = Analysis
    success_message = 'Analysis Updated'


class AnalysisDeleteView(PermissionRequiredMixin, AnalysisSuccessUrlMixin, DeleteView):
    permission_required = 'analyses.delete_analysis'
    model = Analysis
