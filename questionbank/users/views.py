from django.views.generic import ListView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.contrib.auth import get_user_model

User = get_user_model()


class UserListView(PermissionRequiredMixin, ListView):
    permission_required = 'users.view_user'
    model = User
    paginate_by = 20


class UserUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'users.change_user'
    model = User
