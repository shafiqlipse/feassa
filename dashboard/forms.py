from django import forms
from .models import *


class AthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = [
            "fname",
            "lname",
            "gender",
            "date_of_birth",
            "id_number",
            "sport",
            "photo",
        ]
        widgets = {
            "fname": forms.TextInput(attrs={"class": "form-control"}),
            "lname": forms.TextInput(attrs={"class": "form-control"}),
            "id_number": forms.TextInput(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "sport": forms.Select(attrs={"class": "form-control"}),
            "date_of_birth": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }


class OfficialForm(forms.ModelForm):
    class Meta:
        model = Official
        fields = [
            "fname",
            "lname",
            "email",
            "gender",
            "nin",
            "role",
            "school",
            "photo",
        ]
        widgets = {
            "fname": forms.TextInput(attrs={"class": "form-control"}),
            "lname": forms.TextInput(attrs={"class": "form-control"}),
            "nin": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "role": forms.Select(attrs={"class": "form-control"}),
            "school": forms.Select(attrs={"class": "form-control"}),
        }


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ["name", "badge"]


class SchoolTeamForm(forms.ModelForm):
    athletes = forms.ModelMultipleChoiceField(
        queryset=Athlete.objects.all(), widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = SchoolTeam
        fields = [
            "sport",
            "school",
            "gender",
            "athletes",
        ]
        widgets = {
            "athletes": forms.CheckboxSelectMultiple,
        }
