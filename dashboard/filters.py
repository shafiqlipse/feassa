import django_filters
from .models import Athlete


class athleteFilter(django_filters.FilterSet):

    # Add more fields as needed

    class Meta:
        model = Athlete
        fields = [

            "school",
            "sport",
            "gender",
        ]  # Add all fields you want to filter on
