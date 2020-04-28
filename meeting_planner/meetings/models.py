from datetime import time
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=50)
    floor = models.IntegerField()
    room_number = models.IntegerField()

    # def __str__(self):
    #     return self.name, self.room_number, self.floor


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(10))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.title, self.start_time, self.date, self.duration, self.room
