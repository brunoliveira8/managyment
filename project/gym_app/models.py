from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Class to make and test the login/logout system 
class RegularAthlete(models.Model):
    user = models.OneToOneField(User) #Inheritance of User model

<<<<<<< HEAD
class RegularAthlete(Account):
    goalWeight = models.IntegerField(default = 1, max_length=4)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.username+" name: "+self.firstName

class WeightProgress(models.Model):
    startDate = models.DateField(auto_now_add=True)
    startWeight = models.IntegerField(max_length=4)
    previousDate = models.DateField()
    previousWeight = models.IntegerField(max_length=4)
    lastDate = models.DateField(auto_now=True)
    lastWeight = models.IntegerField(max_length=4)
=======
    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.user.username
>>>>>>> login-logout
