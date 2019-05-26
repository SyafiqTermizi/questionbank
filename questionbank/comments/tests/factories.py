from factory import DjangoModelFactory, Faker, SubFactory

from questionbank.exams.tests.factories import ExamFactory
from questionbank.questions.tests.factories import QuestionFactory
from questionbank.users.tests.factories import UserFactory

from questionbank.comments.models import QuestionComment, ExamComment


class QuestionCommentFactory(DjangoModelFactory):
    comment = Faker('paragraph')
    created_by = SubFactory(UserFactory)
    question = SubFactory(QuestionFactory)

    class Meta:
        model = QuestionComment


class ExamCommentFactory(DjangoModelFactory):
    comment = Faker('paragraph')
    created_by = SubFactory(UserFactory)
    exam = SubFactory(ExamFactory)

    class Meta:
        model = ExamComment
