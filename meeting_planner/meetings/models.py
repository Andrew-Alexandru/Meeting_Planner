from datetime import time
from django.db import models


# Create your models here.
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(10))
    duration = models.IntegerField(default=1)
