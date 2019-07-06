from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin

from .mixins import AnalysisSuccessUrlMixin, AnalysisFormMixin
from .models import Analysis


class AnalysisCreateView(PermissionRequiredMixin, AnalysisFormMixin,
                         AnalysisSuccessUrlMixin, CreateView):
    permission_required = 'analyses.add_analysis'
    model = Analysis
    fields = ('passing_index', 'discrimination_index')


class AnalysisUpdateView(PermissionRequiredMixin, AnalysisFormMixin,
                         AnalysisSuccessUrlMixin, UpdateView):
    permission_required = 'analyses.delete_analysis'
    model = Analysis
    fields = ('passing_index', 'discrimination_index')


class AnalysisDeleteView(PermissionRequiredMixin, AnalysisSuccessUrlMixin, DeleteView):
    permission_required = 'analyses.delete_analysis'
    model = Analysis
