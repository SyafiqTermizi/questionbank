from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django_filters.views import FilterView

from .filters import UserFilter

User = get_user_model()


class UserListView(PermissionRequiredMixin, FilterView):
    permission_required = 'users.view_user'
    model = User
    filterset_class = UserFilter
    template_name_suffix = '_list'
    paginate_by = 20


class UserUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'users.change_user'
    model = User
    fields = ('username', 'email')
    success_url = reverse_lazy('users:list')
    success_message = '%(username)s was updated successfully'


class UserProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ('username', 'email')
    template_name = 'users/user_profile.html'
    success_url = reverse_lazy('dashboards:dashboard')
    success_message = '%(username)s was updated successfully'

    def get_object(self):
        obj = User.objects.get(pk=self.request.user.pk)
        return obj


class UserDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'users.delete_user'
    model = User
    success_url = reverse_lazy('users:list')
