from django.contrib import admin
from gym_app.models import Task, RegularAthlete, MailBox, Message
from django.contrib.auth.models import Permission

# Register your models here.
admin.site.register(Task)
admin.site.register(Permission)



