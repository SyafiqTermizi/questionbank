from django.urls import path

from .views import (
    QuestionListView, QuestionCreateView, QuestionUpdateView, QuestionDetailView,
    QuestionDeleteView, QuestionListApiView, TagListApiView, TopicListApiView
)

app_name = 'questions'
urlpatterns = [
    path('', QuestionListView.as_view(), name='list'),
    path('create/', QuestionCreateView.as_view(), name='create'),
    path('<int:pk>/detail/', QuestionDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', QuestionUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', QuestionDeleteView.as_view(), name='delete'),
    path('api/questions/', QuestionListApiView.as_view(), name='api_question_list'),
    path('api/topics/', TopicListApiView.as_view(), name='api_topic_list'),
    path('api/tags/', TagListApiView.as_view(), name='api_tag_list')
]
