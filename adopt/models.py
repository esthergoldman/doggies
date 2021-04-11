from django.db import models
from datetime import datetime
from caretakers.models import Caretaker

class Pet(models.Model):
    caretaker = models.ForeignKey(Caretaker, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=100)
    color = models.CharField(max_length=100,default=True)
    area = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    age = models.CharField(max_length=50,default=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    arrival_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name