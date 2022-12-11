import uuid

from django.db import models


class FormsModel(models.Model):
    name = models.CharField(max_length=200)
    layout = models.TextField()


AppBasicList = [
    ('AppName', 'appname'),
    ('Auth', 'Auth'),
    ('Views', 'Views'),

]


class AppBasic(models.Model):
    config_name = models.CharField(max_length=100, choices=AppBasicList, unique=True)
    value = models.TextField()
    options = models.TextField(blank=True)

class DropDownFieldValues(models.Model) :
    fieldname = models.CharField(max_length=50)
    fieldvalue = models.TextField()


class Criteria(models.Model):
    description = models.CharField(max_length=200)
    criteria = models.TextField()

    def __str__(self):
        return self.description


class CustomView(models.Model):
    Types = [
        (0, 'Project'),
        (1, 'CR'),
        (2, 'Milestone'),
        (3, 'ResourceRequest'),
        (4, 'StakeHolder'),
        (5, 'Dependencies'),
        (6, 'RiskRegister'),
    ]
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    type = models.IntegerField(choices=Types)
    name = models.CharField(max_length=100)
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    is_default = models.BooleanField()