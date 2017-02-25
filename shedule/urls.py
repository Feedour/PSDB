from django.conf.urls import url
from . import views

app_name = 'shedule'

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.index, name='shedule'),
    url(r'^watcher/(?P<pk>[0-9]+)/$', views.DetailWatcher.as_view(), name='watcher'),
]