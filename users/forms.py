from django import forms
from .models import Student

YEARS = [x for x in range(1970, 2019)]


class StudentCreateForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=YEARS[::-1]))

    class Meta:
        model = Student
        fields = ['first_name',
                  'surname',
                  'date_of_birth',
                  'email',
                  'contact_name',
                  'contact_number',
                  'paid'
                  ]
