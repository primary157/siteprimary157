from django.conf.urls import patterns, include, url
from django.contrib import admin
from coisa import views

urlpatterns = patterns('',
    url(r'^testt/', views.index, name='index'),
    # Examples:
<<<<<<< HEAD
    url(r'^$', 'sitetest.views.home', name='home'),
<<<<<<< HEAD
    #url(r'^blog/', include('blog.urls')),
=======
    url(r'^blog/', include('blog.urls')),
=======
    # url(r'^$', 'sitetest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
>>>>>>> parent of 9be75e4... uncomment for testing
>>>>>>> master

    url(r'^admin/', include(admin.site.urls)),
)
