from django.views.generic import ListView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from django.contrib.auth import get_user_model

User = get_user_model()


class UserListView(PermissionRequiredMixin, ListView):
    permission_required = 'users.view_user'
    model = User
    paginate_by = 20


class UserUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'users.change_user'
    model = User
    fields = ('username', 'email')


class UserProfileView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('username', 'email')
    template_name = 'users/user_profile.html'

    def get_object(self):
        obj = User.objects.get(pk=self.request.user.pk)
        return obj
