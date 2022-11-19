from django.db import models

# Create your models here.

class Events(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    description = models.TextField()
    logo = models.FileField()

class Races(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    logo = models.FileField()