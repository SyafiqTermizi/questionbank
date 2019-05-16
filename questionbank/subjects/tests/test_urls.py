from django.urls import reverse, resolve


def test_subject_list():
    assert reverse('subjects:list') == '/subjects/'
    assert resolve('/subjects/').view_name == 'subjects:list'


def test_subject_create():
    assert reverse('subjects:create') == '/subjects/create/'
    assert resolve('/subjects/create/').view_name == 'subjects:create'


def test_subject_update():
    assert reverse('subjects:update', kwargs={'pk': 1}) == '/subjects/1/update/'
    assert resolve('/subjects/1/update/').view_name == 'subjects:update'


def test_subject_delete():
    assert reverse('subjects:delete', kwargs={'pk': 1}) == '/subjects/1/delete/'
    assert resolve('/subjects/1/delete/').view_name == 'subjects:delete'
