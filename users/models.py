from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, is_staff=False, is_superuser=False, **extra_fields):
        if not email:
            raise ValueError('Users must have an email')
        user_obj = self.model(email=self.normalize_email(email))
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.superuser = is_superuser
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password):
        user = self.create_user(email, password, is_staff=True)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password, is_staff=True, is_superuser=True)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=200, unique=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    object = UserManager()


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    surname = models.CharField(max_length=20, null=True)
    date_of_birth = models.DateField(null=True)
    email = models.EmailField(null=True)
    contact_name = models.CharField(max_length=20, null=True)
    contact_number = models.IntegerField(null=True)
    paid = models.NullBooleanField(null=True)
