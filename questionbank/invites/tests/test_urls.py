from django.urls import reverse, resolve


def test_invite_list():
    assert reverse('invites:list') == '/invites/'
    assert resolve('/invites/').view_name == 'invites:list'


def test_invite_create():
    assert reverse('invites:create') == '/invites/create/'
    assert resolve('/invites/create/').view_name == 'invites:create'


def test_invite_delete():
    assert reverse('invites:delete', kwargs={'pk': 1}) == '/invites/1/'
    assert resolve('/invites/1/').view_name == 'invites:delete'
