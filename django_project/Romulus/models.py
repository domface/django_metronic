from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    created_on = models.DateTimeField('date added to portfolio')
    last_updated = models.DateTimeField('last updated')
    logo_url = models.CharField(max_length=500)

class Rounds(models.Model):
    type = models.CharField(max_length=50)
    cash_in =  models.IntegerField(default=0)

