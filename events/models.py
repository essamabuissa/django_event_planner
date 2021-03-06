from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Event(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length = 50)
    capacity = models.IntegerField()
    organizer = models.ForeignKey(User , on_delete = models.CASCADE)
    image = models.ImageField(upload_to = None , blank = True)




    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'event_id':self.id})

class Booking(models.Model):
    event = models.ForeignKey(Event , on_delete = models.CASCADE)
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    tickets = models.IntegerField()
