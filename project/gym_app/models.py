from django.db import models

# Create your models here.

#Abstract class that all user accounts will inherit from
class Account(models.Model):
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    email = models.EmailField(max_length=64)

    class Meta:
        abstract = True

class RegularAthlete(Account):
    goalWeight = models.IntegerField(max_length=4)


class WeightProgress(models.Model):
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

