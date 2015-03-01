from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
<<<<<<< HEAD
    url(r'^$', 'sitetest.views.home', name='home'),
    url(r'^blog/', include('blog.urls')),
=======
    # url(r'^$', 'sitetest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
>>>>>>> parent of 9be75e4... uncomment for testing

    url(r'^admin/', include(admin.site.urls)),
)
