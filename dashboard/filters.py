import django_filters
from .models import Athlete, Official
from accounts.models import NOC

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


class nocFilter(django_filters.FilterSet):

    # Add more fields as needed

    class Meta:
        model = NOC
        fields = [
            "comittee",
            
        ]  # Add all fields you want to filter on
