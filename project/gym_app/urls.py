from django.conf.urls import patterns, url
from gym_app import views

''' You may have seen that within your project configuration directory a urls.py file already exists. 
Why make another? Technically, you can put all the URLs for your project's applications within this file. 
However, this is considered bad practice as it increases coupling on your individual applications. 
A separate urls.py file for each application allows you to set URLs for individual applications. 
With minimal coupling, you can then join them up to your project's master urls.py file later. '''

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))