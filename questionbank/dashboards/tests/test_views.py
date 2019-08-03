import pytest
from django.contrib.auth.models import Group

from questionbank.dashboards.views import Dashboard
from questionbank.users.constants import ADMIN, COORDINATOR, LECTURER

pytestmark = pytest.mark.django_db


def test_get_admin_context(rf, admin_user):
    request = rf.get('/test/')
    request.user = admin_user

    view = Dashboard()
    view.request = request

    context = view.get_context_data()
    assert context['role'] == ADMIN


def test_get_coordinator_context(rf, user, subject):
    coordinator = Group.objects.get(name=COORDINATOR)
    coordinator.user_set.add(user)
    user.course = subject

    request = rf.get('/test/')
    request.user = user

    view = Dashboard()
    view.request = request

    context = view.get_context_data()
    assert context['role'] == COORDINATOR


def test_get_lecturer_context(rf, user):
    lecturer = Group.objects.get(name=LECTURER)
    lecturer.user_set.add(user)

    request = rf.get('/test/')
    request.user = user

    view = Dashboard()
    view.request = request

    context = view.get_context_data()
    assert context['role'] == LECTURER
