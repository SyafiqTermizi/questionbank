import pytest

from questionbank.questions.views import (
    QuestionCreateView, QuestionListView, QuestionDetailView
)

pytestmark = pytest.mark.django_db


def test_question_list_view_get_context_data(rf, user, subject):
    """
    QuestionListView.get_context_data() should return a dict containing
    'courses' key
    """
    request = rf.get('/test/')
    request.user = user

    view = QuestionListView(object_list=[], kwargs={})
    view.request = request

    context = view.get_context_data()
    assert context['courses']


def test_question_create_view_get_context_data(rf, user):
    request = rf.get('/test/')
    request.user = user

    view = QuestionCreateView(object=None)
    view.request = request

    context = view.get_context_data()
    assert context['choices']


def test_question_detail_view_get_context_data(rf, user, question_comment):
    """
    QuestionDetailView.get_context_data() should return number of unresolve comment
    for the question and add it to the context
    """
    request = rf.get('/test/')
    request.user = user

    view = QuestionDetailView()
    view.object = question_comment.question

    context = view.get_context_data()

    assert context['unresolved_comment']
