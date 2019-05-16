from django.shortcuts import reverse
from questionbank.questions.mixins import ChoiceFormMixin


def test_choice_form_mixin():
    """
    calling ChoiceFormMixin.get_success_url() should redirect to question
    detail page
    """
    mixin = ChoiceFormMixin()
    mixin.kwargs = {'question': 1}
    url = mixin.get_success_url()

    assert url == reverse('questions:detail', kwargs={'pk': 1})
