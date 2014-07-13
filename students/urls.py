from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('students.views',
    url(r'^$', 'index'),
    url(r'^add$', 'add_student'),
    url(r'^edit$', 'edit_student'),
    url(r'^delete$', 'delete_student')
)
