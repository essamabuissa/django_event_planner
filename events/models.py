from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField()
    date = models.DateField(auto_now = False)
    time = models.TimeField(auto_now = False)
    location = models.CharField(max_length = 50)
    capacity = models.IntegerField()
