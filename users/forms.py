from django import forms
from .models import Student, Club, Team
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# from .models import User

YEARS = [x for x in range(1970, 2019)]


class StudentCreateForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    surname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=YEARS[::-1]))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    contact_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    contact_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    class Meta:
        model = Student
        fields = ['first_name',
                  'surname',
                  'date_of_birth',
                  'email',
                  'contact_name',
                  'contact_number',
                  'paid',
                  'team'
                  ]


class StudentEditForm(StudentCreateForm):
    class Meta:
        model = Student
        fields = ['first_name',
                  'surname',
                  'surname',
                  'date_of_birth',
                  'email',
                  'contact_name',
                  'contact_number',
                  'team'
                  ]


class ClubCreateForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name']


class TeamCreateForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']


class TeamEditForm(TeamCreateForm):
    class Meta:
        model = Team
        fields = ['name']
