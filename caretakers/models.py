from django.db import models
from datetime import datetime


class Caretaker(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField(default=0)
    area = models.CharField(max_length=100)
    job_position = models.CharField(max_length=100,default=True)
    city = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    join_date = models.DateTimeField(default=datetime.now, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    def __str__(self):
        return self.name