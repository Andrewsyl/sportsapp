from django.db import models
from accounts.models import Club


# Create your models here.
class Timetable(models.Model):
    club = models.ForeignKey(Club, verbose_name=Club, on_delete=models.CASCADE, null=True)


class TimeSlots(models.Model):
    timetable = models.ForeignKey(Timetable, verbose_name=Timetable, on_delete=models.CASCADE, null=True)
