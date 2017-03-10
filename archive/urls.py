from django.conf.urls import url
from . import views

app_name = 'archive'

urlpatterns = [
    url(r'^$', views.index, name='archive'),
    url(r'^person/(?P<pk>[0-9]+)/$', views.person, name='person'),
    url(r'^bg/(?P<pk>[0-9]+)/$', views.bg, name='bg'),
    url(r'^planet/(?P<pk>[0-9]+)/$', views.planet, name='planet'),
    url(r'^mission/(?P<pk>[0-9]+)/$', views.mission, name='mission'),
    ]