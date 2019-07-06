from django.urls import path

from .views import AnalysisCreateView, AnalysisUpdateView, AnalysisDeleteView


app_name = 'analyses'
urlpatterns = [
    path(
        '<int:question_id>/create/',
        AnalysisCreateView.as_view(),
        name='create'
    ),
    path(
        '<int:question_id>/update/<int:pk>/',
        AnalysisUpdateView.as_view(),
        name='update'
    ),
    path(
        '<int:question_id>/delete/<int:pk>/',
        AnalysisDeleteView.as_view(),
        name='delete'
    )
]
