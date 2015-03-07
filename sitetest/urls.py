from django.conf.urls import include, url
from django.contrib import admin
import coisa.views

urlpatterns = [
    url(r'^$', include('inicial.urls')),
    url(r'^poll/', include('poll.urls', namespace="poll")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', coisa.views.index, name='about'),
    url(r'^testt/', include('coisa.urls', namespace="coisa")),
]