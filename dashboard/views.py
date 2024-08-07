from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import *
from .forms import *
from accounts.models import *
from django.contrib import messages
from django.core.files.base import ContentFile
import base64


# Create your views here.
def Dashboard(request):
    athletes_count = Athlete.objects.all().count()
    schools_count = School.objects.all().count()
    official_count = Official.objects.all().count()
    team_count = SchoolTeam.objects.all().count()

    context = {
        "schools_count": schools_count,
        "athletes_count": athletes_count,
        "official_count": official_count,
        "team_count": team_count,
    }
    return render(request, "dashboard/home.html", context)


def AllSchools(request):

    schools = School.objects.all()

    context = {
        "schools": schools,
    }

    return render(request, "school/Allschools.html", context)


def Schools(request):
    user = request.user

    schools = School.objects.filter(user=user)
    new_school = None

    if request.method == "POST":
        cform = SchoolForm(request.POST, request.FILES)

        if cform.is_valid():
            new_school = cform.save(commit=False)
            new_school.user = user
            new_school.country = user.country

            new_school.save()
            return redirect("schools")
    else:
        cform = SchoolForm()

    context = {
        "schools": schools,
        "cform": cform,
    }

    return render(request, "school/schools.html", context)


def SchoolDetail(request, id):
    school = School.objects.get(id=id)
    athletes = Athlete.objects.filter(school=school)
    new_athlete = None

    if request.method == "POST":
        cform = AthleteForm(request.POST, request.FILES)

        if cform.is_valid():
            new_athlete = cform.save(commit=False)
            new_athlete.school = school

            # Handle the cropped image
            if "photo" in request.FILES:
                new_athlete.photo = request.FILES["photo"]

            new_athlete.save()
            messages.success(request, "Athlete added successfully.")
            return redirect("school", school.id)
        else:
            for field, errors in cform.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        cform = AthleteForm()

    context = {
        "school": school,
        "athletes": athletes,
        "cform": cform,
    }

    return render(request, "school/school.html", context)


def athleteDetail(request, id):
    athlete = Athlete.objects.get(id=id)

    context = {
        "athlete": athlete,
    }

    return render(request, "Athletes/athlete.html", context)


def Athletes(request):

    athletes = Athlete.objects.all()

    context = {
        "athletes": athletes,
    }

    return render(request, "Athletes/athletes.html", context)


def athleteUpdate(request, id):
    athlete = get_object_or_404(Athlete, id=id)

    if request.method == "POST":
        cform = AthleteForm(request.POST, request.FILES, instance=athlete)
        if cform.is_valid():
            cform.save()
            return redirect(
                "athletes"
            )  # Replace 'athlete_list' with the name of your list view or any other view
    else:
        cform = AthleteForm(instance=athlete)

    context = {
        "cform": cform,
        "athlete": athlete,
    }

    return render(request, "Athletes/updateathlete.html", context)


def deleteAthlete(request, id):
    athlete = get_object_or_404(Athlete, id=id)

    if request.method == "POST":
        athlete.delete()
        return redirect(
            "athletes"
        )  # Replace 'athlete_list' with the name of your list view or any other view

    context = {
        "athlete": athlete,
    }

    return render(request, "Athletes/deleteathlete.html", context)


def officialDetail(request, id):
    official = Official.objects.get(id=id)

    context = {
        "official": official,
    }

    return render(request, "Officials/official.html", context)


def allOfficials(request):
    user = request.user
    officials = Official.objects.filter(user=user)
    new_official = None

    if request.method == "POST":
        cform = OfficialForm(request.POST, request.FILES)

        if cform.is_valid():
            new_official = cform.save(commit=False)
            new_official.user = user
            # Handle the cropped image
            if "photo" in request.FILES:
                new_official.photo = request.FILES["photo"]

            new_official.save()
            messages.success(request, "Official added successfully.")
            return redirect("allofficials")
        else:
            for field, errors in cform.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        cform = OfficialForm()

    context = {
        "cform": cform,
        "officials": officials,
    }

    return render(request, "Officials/allofficials.html", context)


def Officials(request):

    officials = Official.objects.all()

    context = {
        "officials": officials,
    }

    return render(request, "Officials/officials.html", context)


def officialUpdate(request, id):
    official = get_object_or_404(Official, id=id)

    if request.method == "POST":
        cform = OfficialForm(request.POST, request.FILES, instance=official)
        if cform.is_valid():
            cform.save()
            return redirect(
                "officials"
            )  # Replace 'official_list' with the name of your list view or any other view
    else:
        cform = OfficialForm(instance=official)

    context = {
        "cform": cform,
        "official": official,
    }

    return render(request, "Officials/updateofficial.html", context)


def deleteOfficial(request, id):
    official = get_object_or_404(Official, id=id)

    if request.method == "POST":
        official.delete()
        return redirect(
            "officials"
        )  # Replace 'official_list' with the name of your list view or any other view

    context = {
        "official": official,
    }

    return render(request, "Officials/deleteofficial.html", context)


def create_team(request):
    if request.method == "POST":
        form = SchoolTeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            # Assuming 'school' is the correct attribute name for the school in your Team model
            # Retrieve the school instance associated with the current user
            school_instance = get_object_or_404(School, user=request.user)
            # Assign the school instance to the team
            team.school = school_instance
            team.save()
            athletes = form.cleaned_data.get(
                "athletes"
            )  # Replace 'athletes' with the actual form field name
            team.athletes.set(athletes)
            team.save()

            return redirect("team_s")
        else:
            # Attach errors to the form for display in the template
            error_message = "There was an error in the form submission. Please correct the errors below."
    else:
        form = SchoolTeamForm()
        error_message = None

    return render(
        request, "teams/new_team.html", {"form": form, "error_message": error_message}
    )


# @school_required
def update_team(request, id):
    team = get_object_or_404(SchoolTeam, id=id)

    if request.method == "POST":
        form = SchoolTeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect("teams")  # Redirect to the team list page or another URL
    else:
        form = SchoolTeamForm(instance=team)

    return render(request, "teams/update_team.html", {"form": form, "team": team})


# # view team details


def team_details(request, id):
    team = SchoolTeam.objects.get(id=id)
    athletes = team.athletes.all()
    context = {"team": team, "athletes": athletes}
    return render(request, "teams/team.html", context)


def teamlist(request):
    school_instance = get_object_or_404(School, user=request.user)

    teams = SchoolTeam.objects.filter(school=school_instance)

    context = {"teams": teams}
    return render(request, "teams/teams.html", context)


def allteamlist(request):

    teams = SchoolTeam.objects.all()

    context = {"teams": teams}
    return render(request, "teams/all_teams.html", context)


# # delete team


def delete_team(request, id):
    team = get_object_or_404(SchoolTeam, id=id)

    if request.method == "POST":
        team.delete()
        return redirect("team_s")  # Redirect to the team list page or another URL

    return render(request, "teams/delete_team.html", {"team": team})


from django.http import JsonResponse


def get_athletes(request):
    user = request.user

    gender = request.GET.get("gender")
    sport_id = request.GET.get("sport_id")
    school_id = request.GET.get("school_id")

    athletes = Athlete.objects.all()  # Start with all athletes and filter down

    if school_id:
        athletes = athletes.filter(school_id=school_id)
    if gender:
        athletes = athletes.filter(gender=gender)
    if sport_id:
        athletes = athletes.filter(sport_id=sport_id)

    athletes = athletes.values("id", "fname", "lname")
    data = {"athletes": list(athletes)}

    return JsonResponse(data)


from django.shortcuts import render
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse
from django.contrib.staticfiles import finders
import base64
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.files.storage import default_storage
from xhtml2pdf import pisa
from .models import SchoolTeam


def teamAccreditation(request, id):
    team = SchoolTeam.objects.get(id=id)
    athletes = team.athletes.all()

    # Get template
    template = get_template("albums/acred.html")

    # Compress and fix rotation for athletes' photos

    # Prepare context
    context = {
        "athletes": athletes,
        "MEDIA_URL": settings.MEDIA_URL,
    }

    # Render HTML
    html = template.render(context)

    # Create a PDF
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="Accreditation.pdf"'

    # Generate PDF from HTML
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("We had some errors <pre>" + html + "</pre>")

    return response


def TeamCert(request, id):

    team = SchoolTeam.objects.get(id=id)
    athletes = team.athletes.all()

    # Get template
    template = get_template("albums/cert.html")

    # Prepare context
    context = {
        "athletes": athletes,
        "MEDIA_URL": settings.MEDIA_URL,
    }

    # Render HTML
    html = template.render(context)

    # Create a PDF
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="Certificate.pdf"'

    # Generate PDF from HTML
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("We had some errors <pre>" + html + "</pre>")

    return response


from .filters import *
from xhtml2pdf import pisa
from io import BytesIO


def TAthletes(request):
    # Get all athletes
    athletes = Athlete.objects.all()

    # Apply the filter
    athlete_filter = athleteFilter(request.GET, queryset=athletes)
    filtered_athletes = athlete_filter.qs

    if request.method == "POST":
        # Check which form was submitted
        if "Accreditation" in request.POST:
            template = get_template("teams/sacred.html")
            filename = "Filtered_Accreditation.pdf"
        elif "Certificate" in request.POST:
            template = get_template(
                "teams/certificate_temaplate.html"
            )  # Your certificate template
            filename = "Filtered_Certificate.pdf"
        else:
            return HttpResponse("Invalid form submission")

        # Generate PDF
        context = {"athletes": filtered_athletes}
        html = template.render(context)

        # Create a PDF
        pdf_buffer = BytesIO()
        pisa_status = pisa.CreatePDF(html, dest=pdf_buffer)

        if pisa_status.err:
            return HttpResponse("We had some errors <pre>" + html + "</pre>")

        pdf_buffer.seek(0)

        # Return the PDF as a response
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = f'attachment; filename="{filename}"'
        response.write(pdf_buffer.getvalue())
        return response
    else:
        # Render the filter form
        return render(request, "teams/all_teams.html", {"filter": athlete_filter})


def activity_log_view(request):
    activities = UserActivityLog.objects.all().order_by('-timestamp')
    return render(request, 'dashboard/activity_log.html', {'activities': activities})