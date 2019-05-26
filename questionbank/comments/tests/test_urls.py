from django.urls import reverse, resolve


def test_question_list():
    assert reverse(
        'comments:question_list', kwargs={'question_id': 1}
    ) == '/comments/questions/1/'

    assert resolve('/comments/questions/1/').view_name == 'comments:question_list'


def test_question_create():
    assert reverse(
        'comments:question_create', kwargs={'question_id': 1}
    ) == '/comments/questions/1/create/'
    assert resolve(
        '/comments/questions/1/create/'
    ).view_name == 'comments:question_create'


def test_question_update():
    assert reverse(
        'comments:question_update', kwargs={'question_id': 1, 'pk': 1}
    ) == '/comments/questions/1/update/1/'

    assert resolve(
        '/comments/questions/1/update/1/'
    ).view_name == 'comments:question_update'


def test_question_delete():
    assert reverse(
        'comments:question_delete', kwargs={'question_id': 1, 'pk': 1}
    ) == '/comments/questions/1/delete/1/'

    assert resolve(
        '/comments/questions/1/delete/1/'
    ).view_name == 'comments:question_delete'


def test_question_resolve():
    assert reverse(
        'comments:question_resolve', kwargs={'question_id': 1, 'pk': 1}
    ) == '/comments/questions/1/resolve/1/'

    assert resolve(
        '/comments/questions/1/resolve/1/'
    ).view_name == 'comments:question_resolve'
