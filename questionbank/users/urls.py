from django.urls import path

from .views import (
    UserListView, UserUpdateView, UserProfileView, UserDeleteView,
    AcceptInvitationView
)


app_name = 'users'
urlpatterns = [
    path('', UserListView.as_view(), name='list'),
    path('<int:pk>/', UserUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path(
        'invite/<str:token>/', AcceptInvitationView.as_view(),
        name='accept_invite'
    )
]
