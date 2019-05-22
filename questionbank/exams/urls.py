from django.urls import path

from .views import (
    ExamListView, ExamCreateView, ExamUpdateView, ExamQuestionView,
    ExamDeleteView, ExamPrintView
)


app_name = 'exams'
urlpatterns = [
    path('', ExamListView.as_view(), name='list'),
    path('create/', ExamCreateView.as_view(), name='create'),
    path('<int:pk>/update/', ExamUpdateView.as_view(), name='update'),
    path('<int:pk>/add-question/', ExamQuestionView.as_view(), name='add_question'),
    path('<int:pk>/delete/', ExamDeleteView.as_view(), name='delete'),
    path('<int:pk>/print/', ExamPrintView.as_view(), name='print')
]
