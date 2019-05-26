from django.shortcuts import reverse

from questionbank.comments.mixins import QuestionSuccessUrlMixin


def test_question_success_url_mixin():
    """
    QuestionSuccessUrlMixin.get_success_url() should return url to
    question list with unresolved query param.
    /comments/questions/1/?is_resolved=false
    """
    mixin = QuestionSuccessUrlMixin()
    mixin.kwargs = {'question_id': 1}
    url = mixin.get_success_url()

    assert url == reverse(
        'comments:question_list',
        kwargs={'question_id': 1}
    ) + '?is_resolved=false'
