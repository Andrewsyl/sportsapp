from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from accounts.models import User


class Club(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, null=False)

    def __str__(self):
        return self.name


class Team(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, null=True)
    club = models.ForeignKey(Club, verbose_name=Club, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Create your models here.
class Student(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, null=True)
    surname = models.CharField(max_length=20, null=True)
    date_of_birth = models.DateField(null=True)
    email = models.EmailField(null=True)
    contact_name = models.CharField(max_length=20, null=True)
    contact_number = models.IntegerField(null=True)
    paid = models.NullBooleanField(default=False)


