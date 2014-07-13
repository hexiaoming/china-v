from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('backend.views',
    url(r'^$', 'welcome'),
    url(r'^welcome$', 'welcome'),
    url(r'^login$', 'login'),
    url(r'^logout$', 'logout')
)


