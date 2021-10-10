from django import forms
from django.contrib.auth import password_validation, authenticate
from django.contrib.auth.models import User
from django.forms import ValidationError

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





