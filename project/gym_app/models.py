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

#Class to make and test the login/logout system 
class User(Account):
    
    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.username
