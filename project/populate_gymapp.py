import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()

from gym_app.models import RegularAthlete


def populate():
    RegularAthlete.objects.all().delete()
    add_regularAthlete(firstName = "foo", lastName = "lano", username = "foo1", password = "123", email = "foo@email.com", goalWeight = 200)

    print RegularAthlete.objects.all()



def add_regularAthlete(firstName,lastName, username, password ,email, goalWeight):
    a = RegularAthlete.objects.get_or_create(username = username)[0]
    a.firstName = firstName
    a.lastName=lastName
    a.password = password
    a.email = email
    a.goalWeight = goalWeight
    a.save()
    return a


# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    populate()