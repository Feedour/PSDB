from django.conf.urls import url
from . import views

app_name = 'shedule'

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^login/$', views.enter, name = 'login'),
    url(r'^exit/$', views.exit, name = 'logout'),
    url(r'^(?P<day>[0-9]+)/$', views.shedule, name='shedule'),
    url(r'^(?P<day>[0-9]+)/(?P<pk>[0-9]+)/$', views.lesson, name='lesson'),
    url(r'^(?P<day>[0-9]+)/(?P<pk>[0-9]+)/enroll/$', views.enroll, name='enroll'),
    url(r'^watcher/(?P<pk>[0-9]+)/$', views.DetailWatcher.as_view(), name='watcher'),
]