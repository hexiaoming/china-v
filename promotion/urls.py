from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('promotion.views',
    url(r'^promotion/$', 'index'),
    url(r'^promotion/provet/$','provet'),
    url(r'^promotion/mobvet/$','mobvet'),
    url(r'^promotion/instruction/$','instruction'),
    url(r'^promotion/Vboard/(\d{0,3})/$','Vboard'),
    url(r'^promotion/proerror/$','proerror'),
    url(r'^promotion/pro_mobvet/$','pro_mobvet'),
    url(r'^promotion/vet/(\d{0,3})/$','vet'),
    url(r'^promotion/vet/$','vet'),
    url(r'^promotion/mobvet_post/(\d{0,3})/$','mobvet_post'),
    url(r'^promotion/vboard_show/$','vboard_show'),
    url(r'^promotion/studentlist/$','studentlist')

)


