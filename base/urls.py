from django.conf.urls import patterns, include, url
from django.conf import settings
from django.shortcuts import render, redirect

def index(request):
    return redirect("/static/pages/apppage/index.html");


urlpatterns = patterns('',
    url(r'^ajax-upload/', include('ajax_upload.urls')),
    url(r'^$', index),
    url(r'', include('backend.urls')),
    url(r'^backend/students/', include('students.urls')),
    url(r'^backend/votes/', include('shake.urls')),
    url(r'^students/', include('students.front_urls')),
    url(r'^shake/', include('shake.front_urls')),
    url(r'^', include('promotion.urls'))
)


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
