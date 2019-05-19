from django.urls import reverse, resolve


def test_exam_list():
    assert reverse('exams:list') == '/exams/'
    assert resolve('/exams/').view_name == 'exams:list'


def test_exam_create():
    assert reverse('exams:create') == '/exams/create/'
    assert resolve('/exams/create/').view_name == 'exams:create'
