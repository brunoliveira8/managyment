from django.contrib import admin
from gym_app.models import Task, RegularAthlete, PersonalTrainer, BodyScreening, WorkoutPlan, Tracker, MailBox, Message
from django.contrib.auth.models import Permission

# Register your models here.
admin.site.register(Task)
admin.site.register(Permission)
admin.site.register(RegularAthlete)
admin.site.register(PersonalTrainer)
admin.site.register(BodyScreening)
admin.site.register(WorkoutPlan)
admin.site.register(Tracker)
admin.site.register(MailBox)
admin.site.register(Message)



//
