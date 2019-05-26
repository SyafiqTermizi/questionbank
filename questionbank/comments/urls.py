from django.urls import path

from .views import (
    ExamCommentListView, ExamCommentCreateView, ExamCommentUpdateView,
    ExamCommentDeleteView, ExamCommentResolveView, QuestionCommentListView,
    QuestionCommentCreateView, QuestionCommentUpdateView,
    QuestionCommentDeleteView, QuestionCommentResolveView
)

app_name = 'comments'
urlpatterns = [
    path('exams/<int:exam_id>/', ExamCommentListView.as_view(), name='exam_list'),
    path(
        'exams/<int:exam_id>/create/',
        ExamCommentCreateView.as_view(),
        name='exam_create'
    ),
    path(
        'exams/<int:exam_id>/update/<int:pk>/',
        ExamCommentUpdateView.as_view(),
        name='exam_update'
    ),
    path(
        'exams/<int:exam_id>/delete/<int:pk>/',
        ExamCommentDeleteView.as_view(),
        name='exam_delete'
    ),
    path(
        'exams/<int:exam_id>/resolve/<int:pk>/',
        ExamCommentResolveView.as_view(),
        name='exam_resolve'
    ),

    path(
        'questions/<int:question_id>/',
        QuestionCommentListView.as_view(),
        name='question_list'
    ),
    path(
        'questions/<int:question_id>/create/',
        QuestionCommentCreateView.as_view(),
        name='question_create'
    ),
    path(
        'questions/<int:question_id>/update/<int:pk>/',
        QuestionCommentUpdateView.as_view(),
        name='question_update'
    ),
    path(
        'questions/<int:question_id>/delete/<int:pk>/',
        QuestionCommentDeleteView.as_view(),
        name='question_delete'
    ),
    path(
        'questions/<int:question_id>/resolve/<int:pk>/',
        QuestionCommentResolveView.as_view(),
        name='question_resolve'
    )
]
