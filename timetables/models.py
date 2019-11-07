from django.db import models
from accounts.models import Club


class Day(models.Model):
    club = models.ForeignKey(Club, verbose_name=Club, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Periods(models.Model):
    day = models.ForeignKey(Day, verbose_name=Day, on_delete=models.CASCADE, null=True)
    day_number = models.IntegerField()
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    club = models.ForeignKey(Club, verbose_name=Club, on_delete=models.CASCADE, null=True)

