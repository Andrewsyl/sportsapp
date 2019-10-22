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


def set_field_html_name(cls, new_name):
    """
    This creates wrapper around the normal widget rendering,
    allowing for a custom field name (new_name).
    """
    old_render = cls.widget.render

    def _widget_render_wrapper(name, value, attrs=None):
        return old_render(new_name, value, attrs)

    cls.widget.render = _widget_render_wrapper


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
    # set_field_html_name(start_time, 'start_time_0')
    # set_field_html_name(end_time, 'end_time_0')

    class Meta:
        model = Periods
        fields = ['start_time', 'end_time']
