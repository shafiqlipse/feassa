from django.shortcuts import render, get_object_or_404
from comittee.models import *
from school.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Count
# Create your views here.
@login_required(login_url='login')
def Dashboard(request):
    committees_count = NOC.objects.all().count()
    athletes_count = Athlete.objects.all().count()
    schools_count = School.objects.all().count()
    official_count = Official.objects.all().count()

    # athletes_count = Athlete.objects.all().count()
    kenya_sec_schools = School.objects.filter(country="Kenya",level = "Secondary").count()
    uganda_sec_schools = School.objects.filter(country="Uganda",level = "Secondary").count()
    tanzania_sec_schools = School.objects.filter(country="Tanzania",level = "Secondary").count()
    rwanda_sec_schools = School.objects.filter(country="Rwanda",level = "Secondary").count()
    burundi_sec_schools = School.objects.filter(country="Burundi",level = "Secondary").count()
    # athletes_count = Athlete.objects.all().count()
    kenya_primary_schools = School.objects.filter(country="Kenya",level = "Primary").count()
    uganda_primary_schools = School.objects.filter(country="Uganda",level = "Primary").count()
    tanzania_primary_schools = School.objects.filter(country="Tanzania",level = "Primary").count()
    rwanda_primary_schools = School.objects.filter(country="Rwanda",level = "Primary").count()
    burundi_primary_schools = School.objects.filter(country="Burundi",level = "Primary").count()

    # athletes_count = Athlete.objects.all().count()
    kenya_sec_school = School.objects.filter(country="Kenya",level = "Secondary")
    uganda_sec_school = School.objects.filter(country="Uganda",level = "Secondary")
    tanzania_sec_school = School.objects.filter(country="Tanzania",level = "Secondary")
    rwanda_sec_school = School.objects.filter(country="Rwanda",level = "Secondary")
    burundi_sec_school = School.objects.filter(country="Burundi",level = "Secondary")
    # athletes_count = Athlete.objects.all().count()
    kenya_primary_school = School.objects.filter(country="Kenya",level = "Primary")
    uganda_primary_school = School.objects.filter(country="Uganda",level = "Primary")
    tanzania_primary_school = School.objects.filter(country="Tanzania",level = "Primary")
    rwanda_primary_school = School.objects.filter(country="Rwanda",level = "Primary")
    burundi_primary_school = School.objects.filter(country="Burundi",level = "Primary")
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
    uganda_gsec_school = Athlete.objects.filter(school__in=uganda_sec_school, gender="Female").count()
    uganda_bsec_school = Athlete.objects.filter(school__in=uganda_sec_school, gender="Male").count()
    # rwanda = School.objects.filter(country='Rwanda').count()
    uganda_gpri_school = Athlete.objects.filter(school__in=uganda_primary_school, gender="Female").count()
    uganda_bpri_school = Athlete.objects.filter(school__in=uganda_primary_school, gender="Male").count()
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
        # oficials
        "kenya_sec_schools": kenya_sec_schools,
        "uganda_sec_schools": uganda_sec_schools,
        "tanzania_sec_schools": tanzania_sec_schools,
        "rwanda_sec_schools": rwanda_sec_schools,
        "burundi_sec_schools": burundi_sec_schools,
        # "in_uganda_officials": in_uganda_officials,
        # "in_uganda_officials": in_uganda_officials,
        # oficials
        "uganda_primary_schools": uganda_primary_schools,
        "kenya_primary_schools": kenya_primary_schools,
        "tanzania_primary_schools": tanzania_primary_schools,
        "rwanda_primary_schools": rwanda_primary_schools,
        "burundi_primary_schools": burundi_primary_schools,
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
            "uganda_gsec_school": uganda_gsec_school,
            "uganda_bsec_school": uganda_bsec_school,
            "uganda_gpri_school": uganda_gpri_school,
            "uganda_bpri_school": uganda_bpri_school,
        # "in_burundi_bofficials": in_burundi_bofficials,
        # "in_burundi_bofficials": in_burundi_bofficials,
        "media_from_uganda":media_from_uganda,
    }
    return render(request, "dashboard/overview.html", context)



def album_list(request):
    albums = (
        Athlete.objects
        .values("school_id", "school__name", "sport_id", "sport__name", "gender")
        .annotate(athlete_count=Count("id"))
        .order_by("school__name", "sport__name", "gender")
    )
    return render(request, "albums/list.html", {"albums": albums})


def album_detail(request, school_id, sport_id, gender):
    school = get_object_or_404(School, pk=school_id)
    sport = get_object_or_404(Sport, pk=sport_id)
    athletes = Athlete.objects.filter(
        school_id=school_id, sport_id=sport_id, gender=gender
    ).select_related("school", "sport")
    return render(request, "albums/album_detail.html", {
        "school": school, "sport": sport, "gender": gender, "athletes": athletes,
    })