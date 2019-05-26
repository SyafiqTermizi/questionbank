import pytest

from questionbank.comments.models import QuestionComment
from questionbank.comments.views import QuestionCommentListView, ExamCommentListView

pytestmark = pytest.mark.django_db


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
    """
    QuestionCommentListView.get_queryset() should return ExamComment which limited
    to the Exam object instance
    """
    request = rf.get('/test/')
    request.user = user

    view = QuestionCommentListView()
    view.request = request
    view.kwargs = {'question_id': 1}

    qs = view.get_queryset()

    assert qs != QuestionComment.objects.all()


def test_exam_comment_list_view_get_context_data(user, rf):
    """
    ExamCommentListView.get_context_data() should return a context dict
    with 'exam_id' key
    """
    request = rf.get('/test/')
    request.user = user

    view = ExamCommentListView()
    view.request = request
    view.kwargs = {'exam_id': 1}
    view.object_list = []

    context = view.get_context_data()

    assert context['exam_id'] == 1


def test_exam_comment_list_view_get_queryset(user, rf, exam_comment):
    """
    ExamCommentListView.get_queryset() should return ExamComment which limited
    to the Exam object instance
    """
    request = rf.get('/test/')
    request.user = user

    view = ExamCommentListView()
    view.request = request
    view.kwargs = {'exam_id': 1}

    qs = view.get_queryset()

    assert qs != QuestionComment.objects.all()
