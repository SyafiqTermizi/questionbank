from django.http import Http404
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


def test_question_create_view_get_initial_with_query_param(rf, user, question):
    """
    calling QuestionCreateView() with question query param (/url/?question)
    should return a form with initial data
    """
    url = '/test/?question=' + str(question.pk)
    request = rf.get(url)
    request.user = user

    view = QuestionCreateView()
    view.request = request

    initial = view.get_initial()
    assert initial['course'] == question.course
    assert initial['question'] == question.question


def test_question_create_view_get_initial_with_invalid_query_param(rf, user, question):
    """
    calling QuestionCreateView() with invalid query param should raises Http404
    """
    url = '/test/?question=loljk'
    request = rf.get(url)
    request.user = user

    view = QuestionCreateView()
    view.request = request

    with pytest.raises(Http404):
        view.get_initial()

    url = '/test/?question=99'
    request = rf.get(url)
    request.user = user

    view = QuestionCreateView()
    view.request = request

    with pytest.raises(Http404):
        view.get_initial()


def test_question_create_view_get_initial_without_query_param(rf, user, question):
    """
    calling QuestionCreateView() without question query param (/url/?question)
    should return a form without initial data
    """
    request = rf.get('/test/')
    request.user = user

    view = QuestionCreateView()
    view.request = request

    initial = view.get_initial()
    assert not initial


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
