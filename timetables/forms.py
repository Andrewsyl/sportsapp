from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Day


class TimetableCreateForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = ['day']
