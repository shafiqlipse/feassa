import django_filters
from django import forms
from .models import *

# _+++++++++++++++++Filters++++++++++++++++++++++++++++++
class comitteeFilter(django_filters.FilterSet):
    name = django_filters.ModelMultipleChoiceFilter(
        queryset=NOC.objects.all(),
        label="Name",
        method="filter_by_full_name",
        widget=forms.SelectMultiple(
            attrs={"class": "form-control js-example-basic-multiple-name"}
        )
    )
    title = django_filters.MultipleChoiceFilter(
        choices=lambda: [(n, n) for n in NOC.objects.values_list('title', flat=True).distinct()],
        label="Title",
        widget=forms.SelectMultiple(attrs={"class": "form-control js-example-basic-multiple-name"})
    )
    comittee = django_filters.ChoiceFilter(
        choices=[         ("Technical ", "Technical "),
            ("Welfare ", "Welfare "),
            ("Protocol", "Protocol"),
            ("Finance", "Finance"),
            ("Competitions", "Competitions"),
            ("Medical /Health", "Medical /Health"),
            ("Security and Safety", "Security and Safety"),
            ("Transport", "Transport"),
            ("Corporate Relations", "Corporate Relations"),
            ("Secretariat", "Secretariat"),
            ("Government official", "Government official"),
            ("Executive committee", "Executive committee"),
            ("Sports coordinators", "Sports coordinators"),],
        label="Comittee",
        widget=forms.Select(attrs={"class": "form-control"})
    )

    gender = django_filters.ChoiceFilter(
        choices=[("Male", "Male"), ("Female", "Female")],
        label="Gender",
        widget=forms.Select(attrs={"class": "form-control"})
    )
    # Add more fields as needed

    class Meta:
        model = NOC
        fields = [
            "comittee",
            "gender",
            "title",
            "name",
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Show "First Last" in the dropdown
        self.filters['name'].field.label_from_instance = (
            lambda obj: f"{obj.fname} {obj.lname}"
        )

    def filter_by_full_name(self, queryset, name, value):
        """Filter by selected official IDs, while keeping other filters."""
        if value:
            queryset = queryset.filter(id__in=[v.id for v in value])
        return queryset



# _+++++++++++++++++Filters++++++++++++++++++++++++++++++
class match_official_filter(django_filters.FilterSet):
    name = django_filters.ModelMultipleChoiceFilter(
        queryset=OfficiatingOfficials.objects.all(),
        label="Name",
        method="filter_by_full_name",
        widget=forms.SelectMultiple(
            attrs={"class": "form-control js-example-basic-multiple-name"}
        )
    )
    sport = django_filters.ModelMultipleChoiceFilter(
        queryset=Sport.objects.all(),
        field_name="sport",
        label="Sport",
        widget=forms.SelectMultiple(
            attrs={"class": "form-control js-example-basic-multiple-name"}
        )
    )
    role = django_filters.ChoiceFilter(
        choices=[  
            ("Referee ", "Referee "),
            ("Umpire ", "Umpire "),
            ("Judge", "Judge"),
            ("Assistant Referee", "Assistant Referee"),
            ("Line Umpire", "Line Umpire"),
            ("Timekeeper", "Timekeeper"),
            ("Match Commissioner", "Match Commissioner"),
            ("Finish Judge", "Finish Judge"),
            ("Inspector", "Inspector"),
            ("Anti-Doping Officer", "Anti-Doping Officer"),

],
        label="Role",
        widget=forms.Select(attrs={"class": "form-control"})
    )

    gender = django_filters.ChoiceFilter(
        choices=[("Male", "Male"), ("Female", "Female")],
        label="Gender",
        widget=forms.Select(attrs={"class": "form-control"})
    )
    # Add more fields as needed

    class Meta:
        model = OfficiatingOfficials
        fields = [
            "role",
            "gender",
            "sport",
            "name",
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Show "First Last" in the dropdown
        self.filters['name'].field.label_from_instance = (
            lambda obj: f"{obj.fname} {obj.lname}"
        )

    def filter_by_full_name(self, queryset, name, value):
        """Filter by selected official IDs, while keeping other filters."""
        if value:
            queryset = queryset.filter(id__in=[v.id for v in value])
        return queryset



# _+++++++++++++++++Filters++++++++++++++++++++++++++++++
class mediaFilter(django_filters.FilterSet):

    media_house = django_filters.CharFilter(
                label="Media House  ",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    role = django_filters.ChoiceFilter(
        choices=[     ("Photographer ", "Photographer "),
            ("Editor ", "Editor "),
            ("Writer", "Writer"),
            ("Video Journalist", "Video Journalist"),
            ("Journalist", "Journalist"),
            ("Reporter", "Reporter"),
            ("Radio Journalist", "Radio Journalist"),
            ("Presenter", "Presenter"),
            ("Other", "Other"),
        ],
        label="Role",
        widget=forms.Select(attrs={"class": "form-control"})
    )
    name = django_filters.ModelMultipleChoiceFilter(
        queryset=Media.objects.all(),
        label="Name",
        method="filter_by_full_name",
        widget=forms.SelectMultiple(
            attrs={"class": "form-control js-example-basic-multiple-name"}
        )
    )
    country = django_filters.CharFilter(

        label="Country",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    # Add more fields as needed
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Show "First Last" in the dropdown
        self.filters['name'].field.label_from_instance = (
            lambda obj: f"{obj.fname} {obj.lname}"
        )

    def filter_by_full_name(self, queryset, name, value):
        """Filter by selected official IDs, while keeping other filters."""
        if value:
            queryset = queryset.filter(id__in=[v.id for v in value])
        return queryset
    media_type = django_filters.ChoiceFilter(
        choices=[("NewsPaper ", "NewsPaper "),
            ("Radio ", "Radio "),
            ("Online", "Online"),
            ("Streaming platform", "Streaming platform"),
            ("Television", "Television"),
            ("Tabloid", "Tabloid"),
            ("Blog", "Blog"),
],
        label="Media Type",
        widget=forms.Select(attrs={"class": "form-control"})
    )
    # Add more fields as needed

    class Meta:
        model = Media
        fields = [
            "media_type",
            "name",
            "country",
            "media_house",
        ]  # Add all fields you want to filter on



