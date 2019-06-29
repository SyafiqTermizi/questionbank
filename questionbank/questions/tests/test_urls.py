from django.urls import reverse, resolve


def test_question_list():
    assert reverse('questions:list') == '/questions/'
    assert resolve('/questions/').view_name == 'questions:list'


def test_question_detail():
    assert reverse('questions:detail', kwargs={'pk': 1}) == '/questions/1/detail/'
    assert resolve('/questions/1/detail/').view_name == 'questions:detail'


def test_question_create():
    assert reverse('questions:create') == '/questions/create/'
    assert resolve('/questions/create/').view_name == 'questions:create'


def test_question_update():
    assert reverse('questions:update', kwargs={'pk': 1}) == '/questions/1/update/'
    assert resolve('/questions/1/update/').view_name == 'questions:update'


def test_question_delete():
    assert reverse('questions:delete', kwargs={'pk': 1}) == '/questions/1/delete/'
    assert resolve('/questions/1/delete/').view_name == 'questions:delete'


def test_choice_create():
    assert reverse('questions:choice_create', kwargs={'question': 1}) == '/questions/1/choices/create/'
    assert resolve('/questions/1/choices/create/').view_name == 'questions:choice_create'


def test_choice_update():
    assert reverse(
        'questions:choice_update', kwargs={'question': 1, 'pk': 1}
    ) == '/questions/1/choices/1/update/'

    assert resolve('/questions/1/choices/1/update/').view_name == 'questions:choice_update'


def test_choice_delete():
    assert reverse(
        'questions:choice_delete', kwargs={'question': 1, 'pk': 1}
    ) == '/questions/1/choices/1/delete/'

    assert resolve('/questions/1/choices/1/delete/').view_name == 'questions:choice_delete'
