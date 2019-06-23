from django.shortcuts import reverse

from questionbank.comments.mixins import QuestionSuccessUrlMixin, ExamSuccessUrlMixin


def test_question_success_url_mixin(rf):
    """
    QuestionSuccessUrlMixin.get_success_url() should return url to
    question list with unresolved query param.
    /comments/questions/1/?is_resolved=false
    """
    mixin = QuestionSuccessUrlMixin()
    request = rf.get('/test/')
    mixin.request = request
    mixin.kwargs = {'question_id': 1}
    url = mixin.get_success_url()

    assert url == reverse(
        'comments:question_list',
        kwargs={'question_id': 1}
    ) + '?is_resolved=false'


def test_exam_success_url_mixin():
    """
    ExamSuccessUrlMixin.get_success_url() should return url to
    exam list with unresolved query param.
    /comments/exams/1/?is_resolved=false
    """
    mixin = ExamSuccessUrlMixin()
    mixin.kwargs = {'exam_id': 1}
    url = mixin.get_success_url()

    assert url == reverse(
        'comments:exam_list', kwargs={'exam_id': 1}
    ) + '?is_resolved=false'
