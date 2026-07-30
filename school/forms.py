from django import forms
from django.forms import modelformset_factory
from .models import *


class AthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = [
            "fname",
            "lname",
            "gender",
            "classroom",
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
            "classroom": forms.TextInput(attrs={"class": "form-control"}),
            "sport": forms.Select(attrs={"class": "form-control"}),
            "date_of_birth": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ["name", "level", "badge"]
        widgets = {
             "name": forms.TextInput(attrs={"class": "form-control"}),
                        "level": forms.Select(attrs={"class": "form-control"}),
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
        
        

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['school', 'sport', 'gender', 'position']
        widgets = {

            "position": forms.NumberInput(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "sport": forms.Select(attrs={"class": "form-control js-example-basic-single"}),
            "school": forms.Select(attrs={"class": "form-control js-example-basic-single"}),
        }
        
    def save(self, *args, **kwargs):
        if self.instance.pk:  # Check if this is an existing record
            raise ValueError("Editing saved positions is not allowed.")
        return super().save(*args, **kwargs)
# Create a formset for Position model
PositionFormSet = modelformset_factory(
    Position,
    form=PositionForm,
    extra=1,              # number of empty rows initially
    can_delete=True       # allow deleting rows
)
