from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('shake.views',
    url(r'^$', 'index'),
    url(r'^vote$', 'vote')
)
