import pytest

pytestmark = pytest.mark.django_db


# https://code.djangoproject.com/ticket/17971 (read the last one)
def test_invite_create_view_form_valid(client, mailoutbox, group):
    response = client.post(
        '/invites/create/',
        {
            'username': 'test',
            'email': 'test@test.com',
            'roles': [group]
        }
    )
    # 302 because user is redirected to invite list
    assert response.status_code == 302
