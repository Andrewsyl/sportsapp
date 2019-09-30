from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Day, Periods

DAYS = (
    (1, "Monday"),
    (2, "Tuesday"),
    (3, "Wednesday"),
    (4, "Thursday"),
    (5, "Friday"),
    (6, "Saturday"),
    (7, "Sunday"),
)
HOURS = (('00', '00'), ('05', '05'), ('10', '10'), ('15', '15'), ('20', '20'))


class TimetableCreateForm(forms.ModelForm):
    Days = forms.MultipleChoiceField(choices=DAYS, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Day
        fields = ['Days']


class PeriodCreateForm(forms.ModelForm):
    start_time = forms.ChoiceField(required=False,
                                   choices=HOURS, )
    end_time = forms.ChoiceField(
        required=False,
        choices=HOURS,
    )

    class Meta:
        model = Periods
        fields = ['start_time', 'end_time']