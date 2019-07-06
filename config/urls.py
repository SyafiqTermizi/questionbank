from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views import defaults as default_views

urlpatterns = [
    path('', include('questionbank.dashboards.urls')),
    path('accounts/', include('allauth.urls')),
    path('users/', include('questionbank.users.urls')),
    path('invites/', include('questionbank.invites.urls')),
    path('subjects/', include('questionbank.subjects.urls')),
    path('questions/', include('questionbank.questions.urls')),
    path('exams/', include('questionbank.exams.urls')),
    path('comments/', include('questionbank.comments.urls')),
    path('analysis/', include('questionbank.analyses.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns

    urlpatterns += [
        path(
            '400/', default_views.bad_request,
            kwargs={'exception': Exception('Bad Request!')},
        ),
        path(
            '403/', default_views.permission_denied,
            kwargs={'exception': Exception('Permission Denied')},
        ),
        path(
            '404/', default_views.page_not_found,
            kwargs={'exception': Exception('Page not Found')},
        ),
        path('500/', default_views.server_error),
    ]
