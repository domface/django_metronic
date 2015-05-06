import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    created_on = models.DateTimeField('date added to portfolio')
    last_updated = models.DateTimeField('last updated')
    logo_url = models.CharField(max_length=500)

    def __str__(self):
        return self.name



class Rounds(models.Model):
    type = models.CharField(max_length=50)
    cash_in =  models.IntegerField(default=0)

