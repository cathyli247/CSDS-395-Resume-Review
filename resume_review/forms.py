from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    email = forms.EmailField(required=True, label='Email')
    name = forms.CharField(required=True, label='Name')
    phone_number = forms.CharField(required=True, label='Phone Number')
    major = forms.CharField(required=True, label='Major')
    academic_standing = forms.CharField(required=True, label='Academic Standing')

    username = forms.CharField(required=True, label='Username')
    password1 = forms.CharField(required=True, label='Password')
    password2 = forms.CharField(required=True, label='Confirm password')

class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Username')
    password1 = forms.CharField(required=True, label='Password')
    password2 = forms.CharField(required=True, label='Confirm password')




