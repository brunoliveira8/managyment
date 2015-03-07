from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from gym_app.views import index, register, user_login, user_logout, restricted, workout, edit, change_password, tracker, workout_plan, add_workout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^index/', index),
    url(r'^register/', register), # ADD THIS NEW TUPLE!
    url(r'^login/', user_login), # ADD THIS NEW TUPLE!  
    url(r'^logout/', user_logout), # ADD THIS NEW TUPLE!  
    url(r'^restricted/', restricted),
    url(r'^workout/', workout),
    url(r'^edit/', edit),
    url(r'^change_password/', change_password),
    url(r'^tracker/', tracker),
    url(r'^workout_plan/', workout_plan),
    url(r'^add_workout/', add_workout),
)


if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )