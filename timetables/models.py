from django.db import models
from accounts.models import Club

DAYS = (
    (1, "Monday"),
    (2, "Tuesday"),
    (3, "Wednesday"),
    (4, "Thursday"),
    (5, "Friday"),
    (6, "Saturday"),
    (7, "Sunday"),
)

MINUTES = ()


# Create your models here.
class Day(models.Model):
    club = models.ForeignKey(Club, verbose_name=Club, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, choices=DAYS)


class Periods(models.Model):
    day = models.ForeignKey(Day, verbose_name=Day, on_delete=models.CASCADE, null=True)
    start_time = models.CharField(max_length=200, null=True)
    end_time = models.CharField(max_length=200, null=True)
