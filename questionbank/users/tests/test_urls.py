from django.urls import reverse, resolve


def test_user_list():
    assert reverse('users:list') == '/users/'
    assert resolve('/users/').view_name == 'users:list'


def test_user_update():
    assert reverse('users:update', kwargs={'pk': 1}) == '/users/1/'
    assert resolve('/users/1/').view_name == 'users:update'


def test_user_delete():
    assert reverse('users:delete', kwargs={'pk': 1}) == '/users/1/delete/'
    assert resolve('/users/1/delete/').view_name == 'users:delete'


def test_user_profile():
    assert reverse('users:profile') == '/users/profile/'
    assert resolve('/users/profile/').view_name == 'users:profile'


def test_accept_invite():
    assert reverse('users:accept_invite', kwargs={'token': '123'}) == '/users/invite/123/'
    assert resolve('/users/invite/123/').view_name == 'users:accept_invite'


def test_specialty_list():
    assert reverse('users:specialty_list') == '/users/specialties/'
    assert resolve('/users/specialties/').view_name == 'users:specialty_list'


def test_specialty_create():
    assert reverse('users:specialty_create') == '/users/specialties/create/'
    assert resolve('/users/specialties/create/').view_name == 'users:specialty_create'


def test_specialty_update():
    assert reverse(
        'users:specialty_update', kwargs={'pk': 1}
    ) == '/users/specialties/1/update/'
    assert resolve('/users/specialties/1/update/').view_name == 'users:specialty_update'


def test_specialty_delete():
    assert reverse('users:specialty_delete', kwargs={'pk': 1}) == '/users/specialties/1/delete/'
    assert resolve('/users/specialties/1/delete/').view_name == 'users:specialty_delete'
