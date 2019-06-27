from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django_filters.views import FilterView

from .filters import SubjectFilter
from .models import Subject
from .forms import SubjectForm


class SubjectListView(PermissionRequiredMixin, FilterView):
    permission_required = 'admin'
    model = Subject
    filterset_class = SubjectFilter
    template_name_suffix = '_list'
    paginate_by = 20


class SubjectCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'admin'
    model = Subject
    form_class = SubjectForm
    success_message = '%(code)s is created'
    success_url = reverse_lazy('subjects:list')


class SubjectUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'admin'
    model = Subject
    form_class = SubjectForm
    success_message = '%(code)s is updated'
    success_url = reverse_lazy('subjects:list')


class SubjectDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'admin'
    model = Subject
    success_url = reverse_lazy('subjects:list')
