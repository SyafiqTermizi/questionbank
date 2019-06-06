from django.urls import path

from .views import (
    UserListView, UserUpdateView, UserProfileView, UserDeleteView,
    AcceptInvitationView, SpecialtyListView, SpecialtyCreateView, SpecialtyUpdateView,
    SpecialtyDeleteView
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
    ),
    path('specialties/', SpecialtyListView.as_view(), name='specialty_list'),
    path('specialties/create/', SpecialtyCreateView.as_view(), name='specialty_create'),
    path('specialties/<int:pk>/update/', SpecialtyUpdateView.as_view(), name='specialty_update'),
    path('specialties/<int:pk>/delete/', SpecialtyDeleteView.as_view(), name='specialty_delete')
]
