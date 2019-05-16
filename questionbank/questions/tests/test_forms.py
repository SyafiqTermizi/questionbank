from questionbank.questions.forms import QuestionForm


def test_question_form():
    """
    QuestionForm tags field should not be required
    """
    form = QuestionForm()
    assert not form.fields['tags'].required
