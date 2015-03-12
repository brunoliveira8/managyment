import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()

from gym_app.models import Task


def populate():
    Task.objects.all().delete()
    add_Task(name = "Leg Press", typeTask = "LG")
    add_Task(name = "Chest fly", typeTask = "CH")
    add_Task(name = "Shoulder fly", typeTask = "SH")
    add_Task(name = "Rest", typeTask = "NT")

    print Task.objects.all()

def add_Task(name,typeTask):
    a = Task.objects.get_or_create(name = name)[0]
    a.typeTask = typeTask
    a.save()
    return a


# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    populate()