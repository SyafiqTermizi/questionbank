import pytest
from django.shortcuts import Http404

from ..views import UserProfileView, AcceptInvitationView

pytestmark = pytest.mark.django_db


def test_user_profile_get_obj(user, rf):
    """
    UserProfileView.get_obj() should return a user instance which equal to
    request.user
    """
    request = rf.get('/test/')
    request.user = user

    view = UserProfileView()
    view.request = request

    obj = view.get_object()
    assert obj == user


def test_accept_invite_view_get_token(invite, user, rf):
    """
    AcceptInvitationView.get_token() should return a token
    """
    request = rf.get('/test/')
    request.user = user

    view = AcceptInvitationView(kwargs={'token': invite.token})
    view.request = request

    token = view.get_token()

    assert token == invite.token


def test_accept_invite_view_dispatch(user, rf):
    """
    AcceptInvitationView.dispatch() should raise 404 if the user
    is authenticated
    """
    request = rf.get('/test/')
    request.user = user

    view = AcceptInvitationView()

    with pytest.raises(Http404):
        view.dispatch(request)


def test_accept_invite_view_get_initial(user, specialty, rf):
    """
    AcceptInvitationView.dispatch() should raise 404 if the user
    is authenticated
    """
    request = rf.get('/test/')
    request.user = user

    view = AcceptInvitationView(
        invite_instance={
            'username': 'test_username',
            'email': 'test@email.com',
            'specialty': specialty
        }
    )

    initial = view.get_initial()

    assert initial['username'] == 'test_username'
    assert initial['email'] == 'test@email.com'
