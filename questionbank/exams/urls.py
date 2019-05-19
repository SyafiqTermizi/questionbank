from django.urls import path

from .views import ExamListView, ExamCreateView, ExamUpdateView


app_name = 'exams'
urlpatterns = [
    path('', ExamListView.as_view(), name='list'),
    path('create/', ExamCreateView.as_view(), name='create'),
    path('<int:pk>/update/', ExamUpdateView.as_view(), name='update')
]
