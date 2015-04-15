import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()

from gym_app.models import Task, MailBox
from django.contrib.auth.models import Permission, Group, User
from django.contrib.contenttypes.models import ContentType



def populate():
    Task.objects.all().delete()
    add_Task(name = "Leg Press")
    add_Task(name = "Chest fly")
    add_Task(name = "Shoulder fly")
    add_Task(name = "Squat")
    add_Task(name = "Lunge")
    add_Task(name = "Deadlift")
    add_Task(name = "Leg extension")
    add_Task(name = "Leg curl")
    add_Task(name = "Standing calf raise")
    add_Task(name = "Seated calf raise")
    add_Task(name = "Hip adductor")
    add_Task(name = "Bench press")
    add_Task(name = "Chest fly")
    add_Task(name = "Push-up")
    add_Task(name = "Pulldown")
    add_Task(name = "Pull-up")
    add_Task(name = "Bent-over row")
    add_Task(name = "Upright row")
    add_Task(name = "Shoulder press")
    add_Task(name = "Shoulder fly")
    add_Task(name = "Lateral raise")
    add_Task(name = "Shoulder shrug")
    add_Task(name = "Pushdown")
    add_Task(name = "Triceps extension")
    add_Task(name = "Biceps curl")
    add_Task(name = "Crunch")
    add_Task(name = "Russian twist")
    add_Task(name = "Leg raise")
    add_Task(name = "Back extension")
    add_Task(name = "Rest")

    add_group('regular')
    add_group('premium')
    add_group('personal_trainer')

    add_mail_box('admin')

    add_permission(codename = 'is_admin', name = 'It is admin')
    add_permission(codename = 'is_regular', name = 'It is regular')
    add_permission(codename = 'is_premium', name = 'It is premium')
    add_permission(codename = 'is_personal', name = 'It is personal_trainer')

    group = Group.objects.get(name='regular')
    permission = Permission.objects.get(codename = 'is_regular')
    group.permissions.add(permission)

    group = Group.objects.get(name='premium')
    permission = Permission.objects.get(codename = 'is_premium')
    group.permissions.add(permission)

    group = Group.objects.get(name='personal_trainer')
    permission = Permission.objects.get(codename = 'is_personal')
    group.permissions.add(permission)
    
    admin = User.objects.get(username = 'admin')
    permission = Permission.objects.get(codename = 'is_admin')
    admin.user_permissions.add(permission)


    

    print Task.objects.all()

def add_Task(name):
    a = Task.objects.get_or_create(name = name)[0]
    a.save()
    return a

def add_group(name):
    g = Group.objects.get_or_create(name = name)[0]
    g.save()

def add_permission(codename, name):
    content_type = ContentType.objects.get_for_model(Permission)
    p = Permission.objects.get_or_create(codename = codename, content_type = content_type)[0]
    p.name = name
    p.save()

def add_mail_box(owner):
    g = MailBox.objects.get_or_create(owner = owner)[0]
    g.save()


# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    populate()