import django_filters
from django import forms
from .models import *
from accounts.models import *

# _+++++++++++++++++Filters++++++++++++++++++++++++++++++
class athleteFilter(django_filters.FilterSet):
    school = django_filters.ModelChoiceFilter(
        queryset=School.objects.all(),
        label="School",
        widget=forms.Select(attrs={"class": "form-control js-example-basic-single"})
    )
    sport = django_filters.ModelChoiceFilter(
        queryset=Sport.objects.all(),
        label="Sport",
        widget=forms.Select(attrs={"class": "form-control js-example-basic-single"})
    )
    gender = django_filters.ChoiceFilter(
        choices=[("Male", "Male"), ("Female", "Female")],
        label="Gender",
        widget=forms.Select(attrs={"class": "form-control"})
    )
    # Add more fields as needed

    class Meta:
        model = Athlete
        fields = [
            "school",
            "sport",
            "gender",
        ]


class officialFilter(django_filters.FilterSet):
    school = django_filters.ModelChoiceFilter(
        queryset=School.objects.all(),
        label="School",
        widget=forms.Select(attrs={"class": "form-control js-example-basic-single"})
    )

    gender = django_filters.ChoiceFilter(
        choices=[("Male", "Male"), ("Female", "Female")],
        label="Gender",
        widget=forms.Select(attrs={"class": "form-control"})
    )
    # Add more fields as needed

    class Meta:
        model = Official
        fields = [
            "school",
            "gender",
            "role",
        ]  # Add all fields you want to filter on



