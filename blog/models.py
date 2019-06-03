from django.db import models

# Create your models here.

class Grievance(models.Model):
    name = models.CharField(max_length=20)
    enroll = models.CharField(max_length=20)
    depart = models.BooleanField()
    msg = models.CharField(max_length=200)
    status = models.BooleanField(default=False)