from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Class to make and test the login/logout system 
class User(models.Model):
    user = models.OneToOneField(User) #Inheritance of User model

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.user.username
