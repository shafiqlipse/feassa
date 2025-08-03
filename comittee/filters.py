import django_filters
from django import forms
from .models import *

# _+++++++++++++++++Filters++++++++++++++++++++++++++++++
class comitteeFilter(django_filters.FilterSet):

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
        ]


class mediaFilter(django_filters.FilterSet):


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
    # Add more fields as needed

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
            "role",
        ]  # Add all fields you want to filter on



