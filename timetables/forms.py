from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Day,Periods

DAYS = (
    (1, "Monday"),
    (2, "Tuesday"),
    (3, "Wednesday"),
    (4, "Thursday"),
    (5, "Friday"),
    (6, "Saturday"),
    (7, "Sunday"),
)


class TimetableCreateForm(forms.ModelForm):
    my_field = forms.MultipleChoiceField(choices=DAYS, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Day
        fields = ['my_field']


class PeriodCreateForm(forms.ModelForm):
    my_field = forms.MultipleChoiceField(choices=DAYS, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Periods
        fields = ['my_field']