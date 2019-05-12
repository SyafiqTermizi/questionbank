import pytest

from ..views import UserProfileView

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
