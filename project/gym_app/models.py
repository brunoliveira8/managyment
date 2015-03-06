from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class RegularAthlete(models.Model):
    user = models.OneToOneField(User) #Inheritance of User model
    goal_weight = models.IntegerField(default = 1, max_length=4)
    BEGGINER = 'BG'
    INTERMEDIATE = 'IN'
    ADVANCED = 'AD'
    LEVELS = (
        (BEGGINER, 'Begginer'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
    )
    level = models.CharField(max_length=2,
                                      choices=LEVELS,
                                      default=BEGGINER)

    MORNING = 'MO'
    AFTERNOON = 'AF'
    NIGHT = 'NI'
    TRAINING_PERIOD = (
        (MORNING, 'Morning'),
        (AFTERNOON, 'Afternoon'),
        (NIGHT, 'Night'),
    )
    training_period = models.CharField(max_length=2,
                                      choices=TRAINING_PERIOD,
                                      default=MORNING)
    
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.username+" name: "+self.firstName

class Tracker(models.Model):
    startDate = models.DateField(auto_now_add=True)
    startWeight = models.IntegerField(max_length=4)
    previousDate = models.DateField()
    previousWeight = models.IntegerField(max_length=4)
    lastDate = models.DateField(auto_now=True)
    lastWeight = models.IntegerField(max_length=4)


class Task(models.Model):
    name = models.CharField(max_length=32)
    LEG = 'LG'
    CHEST = 'CH'
    SHOULDER = 'SH'
    NOTYPE = 'NT'
    TYPE_OF_TASKS_CHOICES = (
        (NOTYPE, 'No type'),
        (LEG, 'Leg'),
        (SHOULDER, 'Shoulder'),
        (CHEST, 'Chest'),
    )
    typeTask = models.CharField(max_length=2,
                                      choices=TYPE_OF_TASKS_CHOICES,
                                      default=NOTYPE)

class Exercise(models.Model):
    task = models.ManyToManyField(Task)
    weight = models.IntegerField(max_length=4)
    repetition = models.IntegerField(max_length=4)
    sets = models.IntegerField(max_length=4)

class Workout(models.Model):
    day = models.ManyToManyField(Exercise)


