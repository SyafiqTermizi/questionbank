from django.urls import reverse, resolve


def test_exam_list():
    assert reverse(
        'comments:exam_list', kwargs={'exam_id': 1}
    ) == '/comments/exams/1/'
    assert resolve('/comments/exams/1/').view_name == 'comments:exam_list'


def test_exam_create():
    assert reverse(
        'comments:exam_create', kwargs={'exam_id': 1}
    ) == '/comments/exams/1/create/'
    assert resolve('/comments/exams/1/create/').view_name == 'comments:exam_create'


def test_exam_update():
    assert reverse(
        'comments:exam_update', kwargs={'exam_id': 1, 'pk':1}
    ) == '/comments/exams/1/update/1/'
    assert resolve('/comments/exams/1/update/1/').view_name == 'comments:exam_update'


def test_exam_delete():
    assert reverse(
        'comments:exam_delete', kwargs={'exam_id': 1, 'pk': 1}
    ) == '/comments/exams/1/delete/1/'
    assert resolve('/comments/exams/1/delete/1/').view_name == 'comments:exam_delete'


def test_exam_resolve():
    assert reverse(
        'comments:exam_resolve', kwargs={'exam_id': 1, 'pk': 1}
    ) == '/comments/exams/1/resolve/1/'
    assert resolve('/comments/exams/1/resolve/1/').view_name == 'comments:exam_resolve'


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
