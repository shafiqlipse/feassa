import django_filters
from django import forms
from .models import *
from accounts.models import *

# _+++++++++++++++++Filters++++++++++++++++++++++++++++++
class athleteFilter(django_filters.FilterSet):
    athlete = django_filters.ModelMultipleChoiceFilter(
        queryset=Athlete.objects.all(),
        label="Name",
        method="filter_by_full_name",
        widget=forms.SelectMultiple(
            attrs={"class": "form-control js-example-basic-multiple-name"}
        )
    )
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
            "athlete",
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Show "First Last" in the dropdown
        self.filters['athlete'].field.label_from_instance = (
            lambda obj: f"{obj.fname} {obj.lname}"
        )

    def filter_by_full_name(self, queryset, name, value):
        """Filter by selected athlete IDs, while keeping other filters."""
        if value:
            queryset = queryset.filter(id__in=[v.id for v in value])
        return queryset


class officialFilter(django_filters.FilterSet):
    athlete = django_filters.ModelMultipleChoiceFilter(
        queryset=Official.objects.all(),
        label="Name",
        method="filter_by_full_name",
        widget=forms.SelectMultiple(
            attrs={"class": "form-control js-example-basic-multiple-name"}
        )
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
            "athlete",
        ]  # Add all fields you want to filter on
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Show "First Last" in the dropdown
        self.filters['athlete'].field.label_from_instance = (
            lambda obj: f"{obj.fname} {obj.lname}"
        )

    def filter_by_full_name(self, queryset, name, value):
        """Filter by selected athlete IDs, while keeping other filters."""
        if value:
            queryset = queryset.filter(id__in=[v.id for v in value])
        return queryset
