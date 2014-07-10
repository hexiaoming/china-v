from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('promotion.views',
    url(r'^promotion$', 'index'),
    url(r'^promotion/provet/$','provet'),
    url(r'^promotion/mobvet/$','mobvet'),
    url(r'^promotion/instruction/$','instruction'),
    url(r'^promotion/Vboard/$','Vboard')
)