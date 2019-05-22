from django.urls import reverse, resolve


def test_exam_list():
    assert reverse('exams:list') == '/exams/'
    assert resolve('/exams/').view_name == 'exams:list'


def test_exam_create():
    assert reverse('exams:create') == '/exams/create/'
    assert resolve('/exams/create/').view_name == 'exams:create'


def test_exam_update():
    assert reverse('exams:update', kwargs={'pk': 1}) == '/exams/1/update/'
    assert resolve('/exams/1/update/').view_name == 'exams:update'


def test_exam_delete():
    assert reverse('exams:delete', kwargs={'pk': 1}) == '/exams/1/delete/'
    assert resolve('/exams/1/delete/').view_name == 'exams:delete'


def test_exam_print():
    assert reverse('exams:print', kwargs={'pk': 1}) == '/exams/1/print/'
    assert resolve('/exams/1/print/').view_name == 'exams:print'
