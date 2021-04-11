from django.db import models
from datetime import datetime

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200,blank=True,)
    web = models.URLField(blank=True)
    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    event_date = models.DateTimeField()
    location = models.ForeignKey(Location, blank=True, null=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    organizer = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
