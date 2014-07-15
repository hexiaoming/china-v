from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('students.views',
    url(r'^rank$', 'rank'),
    url(r'^vote$', 'vote')
)