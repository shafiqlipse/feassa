from django import forms
from .models import *


class NocForm(forms.ModelForm):
    class Meta:
        model = NOC
        fields = ["comittee", "fname", "lname", "title","gender", "photo"]
        widgets = {
            "fname": forms.TextInput(attrs={"class": "form-control"}),
            "lname": forms.TextInput(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "comittee": forms.Select(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
        }



class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ["role", "fname", "lname", "media_type", "country", "media_house", "photo"]
        widgets = {
            "fname": forms.TextInput(attrs={"class": "form-control"}),
            "lname": forms.TextInput(attrs={"class": "form-control"}),
            "role": forms.Select(attrs={"class": "form-control"}),
            "country": forms.TextInput(attrs={"class": "form-control"}),
            "media_type": forms.Select(attrs={"class": "form-control"}),
            "media_house": forms.TextInput(attrs={"class": "form-control"}),
        }

