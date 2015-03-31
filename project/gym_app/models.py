from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tracker(models.Model):
    startWeightDate = models.DateField(auto_now_add=True)
    startWeight = models.IntegerField(max_length=4, default=0)
    previousWeightDate = models.DateField(auto_now=True)
    previousWeight = models.IntegerField(max_length=4, default=0)
    currentWeightDate = models.DateField(auto_now=True)
    currentWeight = models.IntegerField(max_length=4, default=170)
    goalWeight = models.IntegerField(default=160, max_length=4)

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
    def __unicode__(self):
        return u'%d' % (self.id)

class WorkoutPlan(models.Model):
    exercises = models.ManyToManyField(Exercise)


class BodyScreening(models.Model):
    screeningDate = models.DateField(auto_now_add=True, default=0)
    triceps = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    biceps = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    subscapular = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    supraspinale = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    suprailic = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    abdominal = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    chest = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    thigh = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    calf = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    weight = models.IntegerField(max_length=4, default=0)
    height = models.IntegerField(max_length=4, default=0)


    EXCELLENT = 'EX'
    GOOD = 'GO'
    AVERAGE = 'AV'
    BELOW_AVERAGE = 'BA'
    POOR = 'PO'
    RESULTS = (
        (EXCELLENT, 'Excellent'),
        (GOOD, 'Good'),
        (AVERAGE, 'Average'),
        (BELOW_AVERAGE, 'Below Average'),
        (POOR, 'Poor'),
    )
    result = models.CharField(max_length=2,
                                      choices=RESULTS,
                                      default=EXCELLENT)


    def __unicode__(self):
        return u'%d' % (self.id)



class RegularAthlete(models.Model):
    user = models.OneToOneField(User) #Inheritance of User model
    tracker = models.OneToOneField(Tracker)
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

    MALE = 'M'
    FEMALE = 'F'
    GENDERS = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    gender = models.CharField(max_length=2,
                                      choices=GENDERS,
                                      default=MALE)

    screenings = models.ManyToManyField(BodyScreening)
    
    def __unicode__(self):
        if self.user.username:
            return u'%s' % (self.user.username)


class PersonalTrainer(models.Model):
    user = models.OneToOneField(User)

    MALE = 'M'
    FEMALE = 'F'
    GENDERS = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    gender = models.CharField(max_length=2,
                                      choices=GENDERS,
                                      default=MALE)








