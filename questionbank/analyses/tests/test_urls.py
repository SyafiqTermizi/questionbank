from django.urls import reverse, resolve


def test_analysis_create():
    assert reverse(
        'analyses:create', kwargs={'question_id': 1}
    ) == '/analysis/1/create/'
    assert resolve('/analysis/1/create/').view_name == 'analyses:create'


def test_analysis_update():
    assert reverse(
        'analyses:update', kwargs={'question_id': 1, 'pk': 1}
    ) == '/analysis/1/update/1/'
    assert resolve('/analysis/1/update/1/').view_name == 'analyses:update'


def test_analysis_delete():
    assert reverse(
        'analyses:delete', kwargs={'question_id': 1, 'pk': 1}
    ) == '/analysis/1/delete/1/'
    assert resolve('/analysis/1/delete/1/').view_name == 'analyses:delete'
