import pytest

from questionbank.users.constants import ADMIN

pytestmark = pytest.mark.django_db


# https://code.djangoproject.com/ticket/17971 (read the last one)
def test_invite_create_view_form_valid(client, mailoutbox):
    response = client.post(
        '/invites/create/',
        {
            'username': 'test',
            'email': 'test@test.com',
            'role': ADMIN
        }
    )
    # 302 because user is redirected to invite list
    assert response.status_code == 302
