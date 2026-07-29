from django import forms
from .models import *


class NocForm(forms.ModelForm):
    class Meta:
        model = NOC
        fields = ["comittee", "fname", "lname", "title", "country", "gender", "photo"]
        widgets = {
            "fname": forms.TextInput(attrs={"class": "form-control", "placeholder": "First name"}),
            "lname": forms.TextInput(attrs={"class": "form-control", "placeholder": "Last name"}),
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Title"}),
            "comittee": forms.Select(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "country": forms.Select(attrs={"class": "form-control"}),
        }




class OfficiatingOfficialsForm(forms.ModelForm):
    class Meta:
        model = OfficiatingOfficials
        fields = ["sport", "fname", "lname", "role","gender","country", "photo"]
        widgets = {
            "fname": forms.TextInput(attrs={"class": "form-control"}),
            "lname": forms.TextInput(attrs={"class": "form-control"}),
            "sport": forms.Select(attrs={"class": "form-control"}),
            "role": forms.Select(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "country": forms.Select(attrs={"class": "form-control"}),
        }



class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ["role", "fname", "lname", "media_type", "country", "media_house", "photo"]
        widgets = {
            "fname": forms.TextInput(attrs={"class": "form-control"}),
            "lname": forms.TextInput(attrs={"class": "form-control"}),
            "role": forms.Select(attrs={"class": "form-control"}),
            "country": forms.Select(attrs={"class": "form-control"}),
            "media_type": forms.Select(attrs={"class": "form-control"}),
            "media_house": forms.TextInput(attrs={"class": "form-control"}),
        }

    