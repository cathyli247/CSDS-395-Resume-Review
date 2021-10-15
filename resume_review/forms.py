from django import forms
from django.contrib.auth import password_validation, authenticate
from django.contrib.auth.models import User
from django.forms import ValidationError, Select

from resume_review import source_api


class RegisterForm(forms.Form):
    username = forms.CharField(required=True, label='Username')
    email = forms.EmailField(required=True)
    password1 = forms.CharField(required=True, label='Password')
    password2 = forms.CharField(required=True, label='Verify password')

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@case.edu'):
            raise ValidationError('Domain of email is not valid')
        return email

    def clean(self):
        password = self.cleaned_data.get('password1')
        re_password = self.cleaned_data.get('password2')
        username = self.cleaned_data.get('username')

        users = User.objects.filter(username=username)
        if len(users) > 0:
            self.add_error('username', "Username has existed")

        if not password == re_password:
            self.add_error('password2', "Passwords must match")

        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Username')
    password = forms.CharField(required=True, label='Password')

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user and username and password:
            users = User.objects.filter(username=username)
            if len(users) == 0:
                self.add_error('username', "Please enter the valid username.")
            else:
                self.add_error('password', "Please enter the valid password.")
        return self.cleaned_data


class UserProfileForm(forms.Form):
    first_name = forms.CharField(required=True, label='First Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}))
    last_name = forms.CharField(required=True, label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}))
    avatar = forms.ImageField(required=False, label='Avatar')
    phone_number = forms.CharField(required=True, label='Phone Number', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}))
    MAJOR_CHOICES = source_api.get_major_list()
    major = forms.ChoiceField(choices=MAJOR_CHOICES, required=True, label='Major',
                              widget=Select(attrs={"class": "form-select"}))
    self_intro = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your self introduction'}))
    price = forms.IntegerField()

    FRESHMEN = 'Freshmen'
    SOPHOMORE = 'Sophomore'
    JUNIOR = 'Junior'
    SENIOR = 'Senior'
    GRADUATE = 'Graduate'

    ACADEMIC_STANDING_CHOICES = [
        (FRESHMEN, 'Freshmen'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]

    academic_standing = forms.ChoiceField(choices=ACADEMIC_STANDING_CHOICES, required=True, label='Academic Standing',
                                          widget=Select(attrs={"class": "form-select"}))
