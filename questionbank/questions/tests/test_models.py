from django.utils.html import mark_safe
from django.shortcuts import reverse
import pytest

pytestmark = pytest.mark.django_db


def test_question_str(question):
    assert mark_safe(question.question) == question.__str__()


def test_question_get_absolute_url(question):
    assert reverse(
        'questions:detail', kwargs={'pk': question.pk}
    ) == question.get_absolute_url()


def test_question_get_unresolve_comment(question_comment):
    """
    calling question.unresolve_comment should return the number of unresolve
    comment
    """
    assert question_comment.question.unresolve_comment == 1


def test_choice_str(choice):
    assert mark_safe(choice.choice) == choice.__str__()


def test_choice_get_absolute_url(choice):
    assert reverse(
        'questions:choice_update', kwargs={'pk': choice.pk, 'question': choice.question.pk}
    ) == choice.get_absolute_url()
