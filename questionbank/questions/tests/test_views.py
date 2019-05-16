import pytest

from questionbank.questions.views import QuestionCreateView, QuestionListView

pytestmark = pytest.mark.django_db


def test_question_list_view_get_context_data(rf, user, subject):
    """
    QuestionListView.get_context_data() should return a dict containing
    'subjects' key
    """
    request = rf.get('/test/')
    request.user = user

    view = QuestionListView(object_list=[], kwargs={})
    view.request = request

    context = view.get_context_data()
    assert context['subjects']


def test_question_create_view_get_context_data(rf, user):
    request = rf.get('/test/')
    request.user = user

    view = QuestionCreateView(object=None)
    view.request = request

    context = view.get_context_data()
    assert context['choices']
