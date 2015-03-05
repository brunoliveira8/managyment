from django.db import models
from django.contrib.auth.models import User

# Create your models here.

<<<<<<< HEAD
class RegularAthlete(models.Model):
    user = models.OneToOneField(User) #Inheritance of User model
    goalWeight = models.IntegerField(default = 1, max_length=4)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.username+" name: "+self.firstName
=======
>>>>>>> workout-model

class WeightProgress(models.Model):
    startDate = models.DateField(auto_now_add=True)
    startWeight = models.IntegerField(max_length=4)
    previousDate = models.DateField()
    previousWeight = models.IntegerField(max_length=4)
    lastDate = models.DateField(auto_now=True)
    lastWeight = models.IntegerField(max_length=4)


class Task(models.Model):
    name = models.CharField(max_length=32)
    typeTask = models.CharField(max_length=32)

class Exercise(models.Model):
    task = models.ManyToManyField(Task)
    weight = models.IntegerField(max_length=4)
    repetition = models.IntegerField(max_length=4)
    sets = models.IntegerField(max_length=4)

class Workout(models.Model):
    day = models.ManyToManyField(Exercise)


