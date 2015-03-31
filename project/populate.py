import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()

from gym_app.models import Task
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType



def populate():
    Task.objects.all().delete()
    add_Task(name = "Leg Press", typeTask = "LG")
    add_Task(name = "Chest fly", typeTask = "CH")
    add_Task(name = "Shoulder fly", typeTask = "SH")
    add_Task(name = "Rest", typeTask = "NT")
    add_group('regular')
    add_group('premium')
    add_group('personal_trainer')

    add_permission(codename = 'is_admin', name = 'It is admin')
    add_permission(codename = 'is_regular', name = 'It is regular')
    add_permission(codename = 'is_premium', name = 'It is premium')
    add_permission(codename = 'is_personal', name = 'It is personal_trainer')
    print Task.objects.all()

def add_Task(name,typeTask):
    a = Task.objects.get_or_create(name = name)[0]
    a.typeTask = typeTask
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


# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    populate()