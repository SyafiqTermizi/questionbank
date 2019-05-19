from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, Http404
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.forms.models import model_to_dict
from django.urls import reverse_lazy
from django_filters.views import FilterView

from questionbank.invites.models import Invite

from .filters import UserFilter
from .forms import UserCreationForm

User = get_user_model()


class UserListView(PermissionRequiredMixin, FilterView):
    permission_required = 'admin'
    model = User
    filterset_class = UserFilter
    template_name_suffix = '_list'
    paginate_by = 20


class UserUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'admin'
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
    permission_required = 'admin'
    model = User
    success_url = reverse_lazy('users:list')


class AcceptInvitationView(FormView):
    form_class = UserCreationForm
    template_name = 'users/acceptance_form.html'
    success_url = reverse_lazy('account_login')
    token = None
    invite_instance = None

    def get_token(self):
        invite = get_object_or_404(Invite, token=self.kwargs['token'])
        self.token = invite.token
        self.invite_instance = model_to_dict(invite)
        return invite.token

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            raise Http404
        self.get_token()
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial['username'] = self.invite_instance['username']
        initial['email'] = self.invite_instance['email']
        initial['specialty'] = self.invite_instance['specialty']
        return initial

    def form_valid(self, form):
        user = form.save()
        group = Group.objects.get(name=self.invite_instance['role'])
        user.groups.add(group)
        Invite.objects.get(token=self.token).delete()
        return super().form_valid(form)
