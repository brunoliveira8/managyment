from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tracker(models.Model):
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
>>>>>>> Stashed changes
    startWeightDate = models.DateField(auto_now_add=True)
    startWeight = models.IntegerField(max_length=4, default=0)
    previousWeightDate = models.DateField(auto_now=True)
    previousWeight = models.IntegerField(max_length=4, default=0)
    currentWeightDate = models.DateField(auto_now=True)
    currentWeight = models.IntegerField(max_length=4, default=100)
    goalWeight = models.IntegerField(default=100, max_length=4)

<<<<<<< Updated upstream
=======
=======
    startDate = models.DateField(auto_now_add=True)
    startWeight = models.IntegerField(max_length=4)
    previousDate = models.DateField()
    previousWeight = models.IntegerField(max_length=4)
    lastDate = models.DateField(auto_now=True)
    lastWeight = models.IntegerField(max_length=4)
>>>>>>> origin/master


>>>>>>> Stashed changes
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

    def __unicode__(self):
        return u'%s' % (self.name)

class Exercise(models.Model):
    task = models.ForeignKey(Task)
    weight = models.IntegerField(max_length=4, default = 1)
    repetition = models.IntegerField(max_length=4, default = 1)
    sets = models.IntegerField(max_length=4, default = 1)

    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    DAYS = (
        (ONE, 'Day 1'),
        (TWO, 'Day 2'),
        (THREE, 'Day 3'),
        (FOUR, 'Day 4'),
        (FIVE, 'Day 5'),
        (SIX, 'Day 6'),
        (SEVEN, 'Day 7'),
    )
    day = models.IntegerField(max_length=7,
                                      choices=DAYS,
                                      default=ONE)

class WorkoutPlan(models.Model):
    
    exercises = models.ManyToManyField(Exercise)


class RegularAthlete(models.Model):
    user = models.OneToOneField(User) #Inheritance of User model
<<<<<<< Updated upstream
    tracker = models.OneToOneField(Tracker)
=======

<<<<<<< HEAD
    tracker = models.OneToOneField(Tracker)
=======
    goal_weight = models.IntegerField(default = 1, max_length=4)
>>>>>>> origin/master

>>>>>>> Stashed changes
    workout_plan = models.OneToOneField(WorkoutPlan)

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
    
    








