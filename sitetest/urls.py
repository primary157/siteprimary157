from django.conf.urls import patterns, include, url
from django.contrib import admin
from coisa import views

urlpatterns = patterns('',
    url(r'^testt/', views.index, name='index'),
    # Examples:
    url(r'^$', 'sitetest.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
