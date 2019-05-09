from django.views.generic import CreateView, ListView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .forms import InviteForm
from .models import Invite


class InviteListView(PermissionRequiredMixin, ListView):
    permission_required = 'invites.view_invite'
    model = Invite
    paginate_by = 20


class InviteCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'invites.add_invite'
    model = Invite
    form_class = InviteForm
    success_url = reverse_lazy('invites:list')
    success_message = '%(username)s Invited'


class InviteDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'invites.delete_bar'
    model = Invite
    success_url = reverse_lazy('invites:list')
