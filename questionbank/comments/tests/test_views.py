import pytest

pytestmark = pytest.mark.django_db

from questionbank.comments.views import QuestionCommentListView
from questionbank.comments.models import QuestionComment


def test_question_comment_list_view_get_context_data(user, rf):
    """
    QuestionCommentListView.get_context_data() should return a context dict
    with 'question_id' key
    """
    request = rf.get('/test/')
    request.user = user

    view = QuestionCommentListView()
    view.request = request
    view.kwargs = {'question_id': 1}
    view.object_list = []

    context = view.get_context_data()

    assert context['question_id'] == 1


def test_question_comment_list_view_get_queryset(user, rf, question_comment):
    request = rf.get('/test/')
    request.user = user

    view = QuestionCommentListView()
    view.request = request
    view.kwargs = {'question_id': 1}

    qs = view.get_queryset()

    assert qs != QuestionComment.objects.all()
