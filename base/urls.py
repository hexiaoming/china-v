from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'^ajax-upload/', include('ajax_upload.urls')),
    url(r'', include('backend.urls')),
    url(r'^backend/students/', include('students.urls')),
    url(r'^backend/votes/', include('shake.urls')),
    url(r'^students/', include('students.front_urls')),
    url(r'^shake/', include('shake.front_urls'))
)


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
