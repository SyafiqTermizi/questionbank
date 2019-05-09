from django.urls import path

from .views import InviteCreateView, InviteListView, InviteDeleteView


app_name = 'invites'
urlpatterns = [
    path('', InviteListView.as_view(), name='list'),
    path('create/', InviteCreateView.as_view(), name='create'),
    path('<int:pk>/', InviteDeleteView.as_view(), name='delete')
]
