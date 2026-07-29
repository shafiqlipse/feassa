from django.shortcuts import render
from comittee.models import *
from school.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def Dashboard(request):
    committees_count = NOC.objects.all().count()
    athletes_count = Athlete.objects.all().count()
    schools_count = School.objects.all().count()
    official_count = Official.objects.all().count()

    # athletes_count = Athlete.objects.all().count()
    kenya_schools = School.objects.filter(country="Kenya")
    uganda_schools = School.objects.filter(country="Uganda")
    tanzania_schools = School.objects.filter(country="Tanzania")
    rwanda_schools = School.objects.filter(country="Rwanda")
    burundi_schools = School.objects.filter(country="Burundi")

    # rwanda = School.objects.filter(country='Rwanda').count()
    in_uganda_officials = Official.objects.filter(school__in=uganda_schools).count()
    in_kenya_officials = Official.objects.filter(school__in=kenya_schools).count()
    in_tanzania_officials = Official.objects.filter(school__in=tanzania_schools).count()
    in_rwanda_officials = Official.objects.filter(school__in=rwanda_schools).count()
    in_burundi_officials = Official.objects.filter(school__in=burundi_schools).count()
    # rwanda = School.objects.filter(country='Rwanda').count()
    # rwanda = School.objects.filter(country='Rwanda').count()
    in_uganda_athletes = Athlete.objects.filter(school__in=uganda_schools).count()
    in_kenya_athletes = Athlete.objects.filter(school__in=kenya_schools).count()
    in_tanzania_athletes = Athlete.objects.filter(school__in=tanzania_schools).count()
    in_rwanda_athletes = Athlete.objects.filter(school__in=rwanda_schools).count()
    in_burundi_athletes = Athlete.objects.filter(school__in=burundi_schools).count()
    # rwanda = School.objects.filter(country='Rwanda').count()

    # rwanda = School.objects.filter(country='Rwanda').count()
    in_uganda_gofficials = Official.objects.filter(
        school__in=uganda_schools, gender="Female"
    ).count()
    in_uganda_bofficials = Official.objects.filter(
        school__in=uganda_schools, gender="Male"
    ).count()
    in_kenya_gofficials = Official.objects.filter(
        school__in=kenya_schools, gender="Female"
    ).count()
    in_kenya_bofficials = Official.objects.filter(
        school__in=kenya_schools, gender="Male"
    ).count()
    in_tanzania_gofficials = Official.objects.filter(
        school__in=tanzania_schools, gender="Female"
    ).count()
    in_tanzania_bofficials = Official.objects.filter(
        school__in=tanzania_schools, gender="Male"
    ).count()
    in_rwanda_gofficials = Official.objects.filter(
        school__in=rwanda_schools, gender="Female"
    ).count()
    in_rwanda_bofficials = Official.objects.filter(
        school__in=rwanda_schools, gender="Male"
    ).count()
    in_burundi_gofficials = Official.objects.filter(
        school__in=burundi_schools, gender="Female"
    ).count()
    in_burundi_bofficials = Official.objects.filter(
        school__in=burundi_schools, gender="Male"
    ).count()
    # rwanda = School.objects.filter(country='Rwanda').count()
    kenya = School.objects.filter(country="Kenya").count()
    uganda = School.objects.filter(country="Uganda").count()
    tanzania = School.objects.filter(country="Tanzania").count()
    rwanda = School.objects.filter(country="Rwanda").count()
    burundi = School.objects.filter(country="Burundi").count()

    # team_count = SchoolTeam.objects.all().count()
    in_uganda_schools = Athlete.objects.filter(school__in=uganda_schools).count()
    in_uganda_girls = Athlete.objects.filter(
        school__in=uganda_schools, gender="Female"
    ).count()
    in_uganda_boys = Athlete.objects.filter(
        school__in=uganda_schools, gender="Male"
    ).count()
    in_kenya_schools = Athlete.objects.filter(school__in=kenya_schools).count()
    in_kenya_girls = Athlete.objects.filter(
        school__in=kenya_schools, gender="Female"
    ).count()
    in_kenya_boys = Athlete.objects.filter(
        school__in=kenya_schools, gender="Male"
    ).count()
    in_tanzania_schools = Athlete.objects.filter(school__in=tanzania_schools).count()
    in_tanzania_girls = Athlete.objects.filter(
        school__in=tanzania_schools, gender="Female"
    ).count()
    in_tanzania_boys = Athlete.objects.filter(
        school__in=tanzania_schools, gender="Male"
    ).count()
    in_rwanda_schools = Athlete.objects.filter(school__in=rwanda_schools).count()
    in_burundi_schools = Athlete.objects.filter(school__in=burundi_schools).count()
    in_rwanda_girls = Athlete.objects.filter(
        school__in=rwanda_schools, gender="Female"
    ).count()
    in_rwanda_boys = Athlete.objects.filter(
        school__in=rwanda_schools, gender="Male"
    ).count()
    in_burundi_girls = Athlete.objects.filter(
        school__in=burundi_schools, gender="Female"
    ).count()
    in_burundi_boys = Athlete.objects.filter(
        school__in=burundi_schools, gender="Male"
    ).count()
    # media officials and journalists in different countries
    media_from_uganda = Media.objects.filter(country = "Uganda").count
    context = {
        "schools_count": schools_count,
        "athletes_count": athletes_count,
        "official_count": official_count,
        "committees_count": committees_count,
        # oficials
        "in_uganda_officials": in_uganda_officials,
        "in_kenya_officials": in_kenya_officials,
        "in_tanzania_officials": in_tanzania_officials,
        "in_rwanda_officials": in_rwanda_officials,
        "in_burundi_officials": in_burundi_officials,
        # "in_uganda_officials": in_uganda_officials,
        "kenya": kenya,
        "uganda": uganda,
        "tanzania": tanzania,
        "rwanda": rwanda,
        "burundi": burundi,
        #school
        "in_uganda_schools": in_uganda_schools,
        "in_kenya_schools": in_kenya_schools,
        "in_tanzania_schools": in_tanzania_schools,
        "in_rwanda_schools": in_rwanda_schools,
        "in_burundi_schools": in_burundi_schools,
        # "in_rwanda_schools": in_rwanda_schools,
        # athletes
        "in_uganda_athletes": in_uganda_athletes,
        "in_kenya_athletes": in_kenya_athletes,
        "in_tanzania_athletes": in_tanzania_athletes,
        "in_rwanda_athletes": in_rwanda_athletes,
        "in_burundi_athletes": in_burundi_athletes,
        # "in_rwanda_athletes": in_rwanda_athletes,
        # "in_rwanda_schools": in_rwanda_schools,
        "in_uganda_girls": in_uganda_girls,
        "in_kenya_girls": in_kenya_girls,
        "in_tanzania_girls": in_tanzania_girls,
        "in_rwanda_girls": in_rwanda_girls,
        "in_burundi_girls": in_burundi_girls,
        "in_uganda_boys": in_uganda_boys,
        "in_kenya_boys": in_kenya_boys,
        "in_tanzania_boys": in_tanzania_boys,
        "in_rwanda_boys": in_rwanda_boys,
        "in_burundi_boys": in_burundi_boys,
        # "in_rwanda_boys": in_rwanda_boys,
        "in_uganda_gofficials": in_uganda_gofficials,
        "in_uganda_bofficials": in_uganda_bofficials,
        "in_kenya_gofficials": in_kenya_gofficials,
        "in_kenya_bofficials": in_kenya_bofficials,
        "in_tanzania_gofficials": in_tanzania_gofficials,
        "in_tanzania_bofficials": in_tanzania_bofficials,
        "in_rwanda_gofficials": in_rwanda_gofficials,
        "in_burundi_gofficials": in_burundi_gofficials,
        "in_rwanda_bofficials": in_rwanda_bofficials,
        "in_burundi_bofficials": in_burundi_bofficials,
        # "in_burundi_bofficials": in_burundi_bofficials,
        "media_from_uganda":media_from_uganda,
    }
    return render(request, "dashboard/overview.html", context)

