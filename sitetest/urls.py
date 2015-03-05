from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
import coisa.views

urlpatterns = patterns('',
    url(r'^$', include('inicial.urls')),
    url(r'^poll/', include('poll.urls')),
    url(r'^about/', coisa.views.index, name='about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^testt/', include('coisa.urls')),
)
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
