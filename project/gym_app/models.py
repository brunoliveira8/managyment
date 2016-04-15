from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

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
    name = models.CharField(max_length=256)

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
    screeningDate = models.DateField(default=datetime.now)
    triceps = models.IntegerField(max_length=3, default=0)
    biceps = models.IntegerField(max_length=3, default=0)
    subscapular = models.IntegerField(max_length=3, default=0)
    supraspinale = models.IntegerField(max_length=3, default=0)
    suprailic = models.IntegerField(max_length=3, default=0)
    abdominal = models.IntegerField(max_length=3, default=0)
    chest = models.IntegerField(max_length=3, default=0)
    thigh = models.IntegerField(max_length=3, default=0)
    calf = models.IntegerField(max_length=3, default=0)
    weight = models.IntegerField(max_length=4, default=0)
    feet = models.IntegerField(max_length=4, default=0)
    inches = models.IntegerField(max_length=4, default=0)
    bodyfat = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    bmi = models.DecimalField(max_digits=6, decimal_places=1, default=0)
    def __unicode__(self):
        return u'%d' % (self.id)



class Athlete(models.Model):
    user = models.OneToOneField(User) #Inheritance of User model
    tracker = models.OneToOneField(Tracker)
    workout_plan = models.OneToOneField(WorkoutPlan)

    BEGGINER = 'BG'
    INTERMEDIATE = 'IN'
    ADVANCED = 'AD'
    LEVELS = (
        (BEGGINER, 'Beginner'),
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

#Message System
class Message(models.Model):
    sbj = models.CharField(max_length=50)
    body = models.TextField(max_length = 500)
    src = models.CharField(max_length=50)


class MailBox(models.Model):
    owner = models.CharField(max_length=50)
    messages = models.ManyToManyField(Message)

    def add_msg(self, body, sbj, src):
        self.messages.create(body = body, sbj = sbj, src = src)

    def get_msg(self):
        pass

    def del_msg(self, id):
        Message.objects.filter(id = id).delete()

#end Message System

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








