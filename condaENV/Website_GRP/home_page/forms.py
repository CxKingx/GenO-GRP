from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo


# this is for asking forms from models we have created

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')  # can add first name last name


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('StudentID',)
