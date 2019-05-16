from django.views.generic import CreateView, ListView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail

from allauth.utils import build_absolute_uri

from .forms import InviteForm
from .models import Invite


class InviteListView(PermissionRequiredMixin, ListView):
    permission_required = 'admin'
    model = Invite
    paginate_by = 20


class InviteCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'admin'
    model = Invite
    form_class = InviteForm
    success_url = reverse_lazy('invites:list')
    success_message = '%(username)s Invited'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        self.object = form.save()
        path = reverse('users:accept_invite', kwargs={'token': self.object.token})
        url = build_absolute_uri(self.request, path)

        send_mail(
            subject='Invitation to Medic Putra Qbank',
            message=url,
            from_email='admin@example.com',
            recipient_list=[self.object.email]
        )
        return super().form_valid(form)


class InviteDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'admin'
    model = Invite
    success_url = reverse_lazy('invites:list')
