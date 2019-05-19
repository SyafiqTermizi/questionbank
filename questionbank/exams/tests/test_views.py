import pytest

from questionbank.exams.views import ExamCreateView, ExamQuestionView

pytestmark = pytest.mark.django_db


def test_exam_create_view_get_success_url(rf, user, exam):
    """
    ExamCreateView.get_success_url() should redirect the user either to
    exam list view or add question view depending on the user input
    """
    request = rf.get('/test/')
    request.user = user

    view = ExamCreateView()
    view.request = request

    url = view.get_success_url()

    # the view should redirect user to exam list view if the user
    # click submit
    assert url == '/exams/'

    view = ExamCreateView()
    view.request = request
    view.request.POST = {'next': True}
    view.object = exam
    url = view.get_success_url()

    # the view should redirect user to add question view if the user
    # click add question
    assert url == '/exams/' + str(exam.pk) + '/add-question/'


def test_exam_question_view(rf, user, exam):
    """
    ExamQuestionView.get_form_kwargs() should add 'subject' key to form kwargs
    """
    request = rf.get('/test/')
    request.user = user

    view = ExamQuestionView()
    view.request = request
    view.object = exam

    kwargs = view.get_form_kwargs()

    assert kwargs['subject']
