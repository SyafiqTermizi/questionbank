from django.urls import path

from .views import (
    QuestionListView, QuestionCreateView, QuestionUpdateView,
    QuestionDetailView, QuestionDeleteView, ChoiceCreateView,
    ChoiceUpdateView, ChoiceDeleteView
)

app_name = 'questions'
urlpatterns = [
    path('', QuestionListView.as_view(), name='list'),
    path('create/', QuestionCreateView.as_view(), name='create'),
    path('<int:pk>/detail/', QuestionDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', QuestionUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', QuestionDeleteView.as_view(), name='delete'),

    path(
        '<int:question>/choices/create/', ChoiceCreateView.as_view(),
        name='choice_create'
    ),
    path(
        '<int:question>/choices/<int:pk>/update/', ChoiceUpdateView.as_view(),
        name='choice_update'
    ),
    path(
        '<int:question>/choices/<int:pk>/delete/', ChoiceDeleteView.as_view(),
        name='choice_delete'
    )

]
