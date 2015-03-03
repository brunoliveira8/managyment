from django.conf.urls import patterns, url
from gym_app import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))