from django import forms
from .models import *


class NocForm(forms.ModelForm):
    class Meta:
        model = NOC
        fields = ["comittee", "fname", "lname", "title", "photo"]
        widgets = {
            "fname": forms.TextInput(attrs={"class": "form-control"}),
            "lname": forms.TextInput(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "comittee": forms.Select(attrs={"class": "form-control"}),
        }


# class SchoolForm(forms.ModelForm):
#     class Meta:
#         model = School
#         fields = ["name", "badge"]


from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import User


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=100)
    phone = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "phone",
            "username",
            "password1",
            "password2",
        ]
