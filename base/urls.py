from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
<<<<<<< HEAD
    url(r'^ajax-upload/', include('ajax_upload.urls')),
    url(r'', include('backend.urls')),
    url(r'^backend/students/', include('students.urls')),
    url(r'^students/', include('students.front_urls'))
=======
    # Examples:
    # url(r'^$', 'chinav.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('backend.urls')),
    url(r'^', include('promotion.urls'))
>>>>>>> 5db5252e9e3ef21cfef65789b52cb81845c78c99
)


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
