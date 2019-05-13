from django.urls import path

from .views import (
    SubjectListView, SubjectCreateView, SubjectUpdateView, SubjectDeleteView
)

app_name = 'subjects'
urlpatterns = [
    path('', SubjectListView.as_view(), name='list'),
    path('create/', SubjectCreateView.as_view(), name='create'),
    path('<int:pk>/update/', SubjectUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', SubjectDeleteView.as_view(), name='delete')
]
