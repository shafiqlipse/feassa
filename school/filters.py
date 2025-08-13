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
    fname = django_filters.MultipleChoiceFilter(
        choices=lambda: [(n, n) for n in Official.objects.values_list('fname', flat=True).distinct()],
        label="Name",
        widget=forms.SelectMultiple(attrs={"class": "form-control js-example-basic-multiple-name"})
    )
    school = django_filters.ModelChoiceFilter(
        queryset=School.objects.all(),
        label="School",
        widget=forms.Select(attrs={"class": "form-control js-example-basic-single"})
    )

    role = django_filters.ChoiceFilter(
        choices=[     ("Coach", "Coach"),
            ("Games teacher", "Games teacher"),
            ("Head of delegation", "Head of delegation"),
            ("Field of play officer", "Field of play officer"),
            ("Medical", "Medical"),
            ("Security", "Security"),
            ("Young reporter", "Young reporter"),
            ("Press", "Press"),
            ("Volunteer", "Volunteer"),
            ("President", "President"),
            ("Secretary General", "Secretary General"),
            ("Treasurer", "Treasurer"),
            ("Sports coordinators", "Sports coordinators"),
            ("Matron", "Matron"),
            ("Patron", "Patron"),
            ("Chaperone", "Chaperone"),
            ("Sight guide", "Sight guide"),
            ("Sign language interpreter", "Sign language interpreter"),
            ("Team Manager", "Team Manager"),
            ("Other", "Other"),],
        label="Gender",
        widget=forms.Select(attrs={"class": "form-control"})
    )
    # Add more fields as needed

    class Meta:
        model = Official
        fields = [
            "school",
            "role",
            "fname",
        ]  # Add all fields you want to filter on



