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
