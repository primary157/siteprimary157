from django.conf.urls import patterns, url
import inicial.views

urlpatterns = patterns('',
	url(r'^$', inicial.views.algo, name='index'),
)