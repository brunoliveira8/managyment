from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from gym_app.views import *


admin.site.site_title = 'MANAGYMENT'
admin.site.site_index = 'MANAGYMENT'
admin.site.site_header = 'DASHBOARD'


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
    url(r'^edit/', edit),
    url(r'^change_password/', change_password),
    url(r'^tracker/', tracker),
    url(r'^members/', members),
    url(r'^send/', message),
    url(r'^buddy_match/', buddy_match),
    url(r'^send_match/', message_match),
    url(r'^workout_plan/', workout_plan),
    url(r'^workout/days/(?P<day>\d{1})/$', workout_day),
    url(r'^delete_exercise/', delete_exercise),
    url(r'^upgrade_downgrade/', upgrade_downgrade),
    url(r'^plan_manage/', plan_manage),
    url(r'^permission_denied/', permission_denied),
    url(r'^delete_plan_msg/', delete_plan_msg),
    url(r'^change_upgrade_downgrade/', change_upgrade_downgrade),
    url(r'^payment/', payment),
    url(r'^screenings/', screenings),
    url(r'^create_screening/', create_screening),    
    url(r'^delete_screening/', delete_screening),    
    url(r'^manage_workout/', manage_workout),

)


if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )