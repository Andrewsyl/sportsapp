from django import forms
from .models import Student
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

YEARS = [x for x in range(1970, 2019)]


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('full_name', 'email',)

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     qs = User.objects.filter(email=email)
    #     if qs.exists():
    #         raise forms.ValidationError("email is taken")
    #     return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('full_name', 'email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class Login(forms.Form):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={
        'class': 'form-control','placeholder': 'Username'
    }))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={
        'class': 'form-control','placeholder': 'Password'
    }))

    # email = forms.EmailField(required=True)
    # password = forms.CharField(widget=forms.PasswordInput)


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('full_name', 'email', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


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
                  'paid'
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
                  ]
