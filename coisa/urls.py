from django.conf.urls import patterns, url
from sitetest import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
)
