from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('shake.front_views',
    url(r'^$', 'index'),
    url(r'^rank$', 'rank'),
    url(r'^lottery$', 'lottery')
)
