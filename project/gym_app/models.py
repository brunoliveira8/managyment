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

