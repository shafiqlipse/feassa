import django_filters
from .models import Athlete, Official


class athleteFilter(django_filters.FilterSet):

    # Add more fields as needed

    class Meta:
        model = Athlete
        fields = [
            "school",
            "sport",
            "gender",
        ]


class officialFilter(django_filters.FilterSet):

    # Add more fields as needed

    class Meta:
        model = Official
        fields = [
            "school",
            "gender",
        ]  # Add all fields you want to filter on
