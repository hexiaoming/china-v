from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('promotion.views',
    url(r'^promotion/$', 'index'),
    url(r'^promotion/provet/$','provet'),
    url(r'^promotion/mobvet/$','mobvet'),
    url(r'^promotion/instruction/$','instruction'),
    url(r'^promotion/Vboard/$','Vboard'),
    url(r'^promotion/proerror/$','proerror'),
    url(r'^promotion/pro_mobvet/$','pro_mobvet'),
    url(r'^promotion/vet/$','vet')
)


