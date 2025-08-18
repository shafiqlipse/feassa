from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import *
from .forms import *
from accounts.models import *
from django.contrib import messages
from django.core.files.base import ContentFile
import base64
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def AllSchools(request):

    schools = School.objects.all()

    context = {
        "schools": schools,
    }

    return render(request, "school/Allschools.html", context)

@login_required(login_url='login')
def Schools(request):
    user = request.user
    schools = School.objects.filter(user=user)
    new_school = None
    school_to_edit = None

    # Check if we're editing
    school_id = request.GET.get("edit") or request.POST.get("school_id")
    if school_id:
        school_to_edit = get_object_or_404(School, id=school_id, user=user)

    if request.method == "POST":
        if school_to_edit:
            cform = SchoolForm(request.POST, request.FILES, instance=school_to_edit)
        else:
            cform = SchoolForm(request.POST, request.FILES)

        if cform.is_valid():
            new_school = cform.save(commit=False)
            if not school_to_edit:  # Only set these when creating
                new_school.user = user
                new_school.country = user.country
            new_school.save()
            return redirect("schools")
    else:
        if school_to_edit:
            cform = SchoolForm(instance=school_to_edit)
        else:
            cform = SchoolForm()

    context = {
        "schools": schools,
        "cform": cform,
        "school_to_edit": school_to_edit,
    }

    return render(request, "school/schools.html", context)


@login_required(login_url='login')
def SchoolDetail(request, id):
    school = get_object_or_404(School, id=id)
    athletes = Athlete.objects.filter(school=school)
    new_athlete = None

    if request.method == "POST":
        cform = AthleteForm(request.POST, request.FILES)

        if cform.is_valid():
            new_athlete = cform.save(commit=False)
            new_athlete.school = school

            # Handle the cropped image
            cropped_data = request.POST.get("photo_cropped")
            if cropped_data:
                try:
                    format, imgstr = cropped_data.split(";base64,")
                    ext = format.split("/")[-1]
                    data = ContentFile(
                        base64.b64decode(imgstr), name=f"photo.{ext}"
                    )
                    new_athlete.photo = data
                except (ValueError, TypeError):
                    messages.error(request, "Invalid image data.")
                    return render(
                        request, "athletes/newAthlete.html", {"cform": cform}
                    )

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

# _+++++++++++++++++Athletes++++++++++++++++++++++++++++++

def athleteDetail(request, id):
    athlete = Athlete.objects.get(id=id)

    context = {
        "athlete": athlete,
    }

    return render(request, "athletes/athlete.html", context)
# _+++++++++++++++++Athletes++++++++++++++++++++++++++++++

def qr_code(request, id):
    athlete = Athlete.objects.get(id=id)
    context = {
        "athlete": athlete,
    }
    return render(request, "athletes/qr_code.html", context)

@login_required(login_url='login')
def Athletes(request):

    athletes = Athlete.objects.all()

    context = {
        "athletes": athletes,
    }

    return render(request, "athletes/athletes.html", context)

@login_required(login_url='login')
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

    return render(request, "athletes/updateathlete.html", context)

@login_required(login_url='login')
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

    return render(request, "athletes/deleteathlete.html", context)


# _+++++++++++++++++Officials++++++++++++++++++++++++++++++
@login_required(login_url='login')
def officialDetail(request, id):
    official = Official.objects.get(id=id)

    context = {
        "official": official,
    }

    return render(request, "Officials/official.html", context)

@login_required(login_url='login')
def allOfficials(request):
    user = request.user
    officials = Official.objects.filter(user=user)
    new_official = None

    if request.method == "POST":
        cform = OfficialForm(request.POST, request.FILES)

        if cform.is_valid():
            new_official = cform.save(commit=False)
            new_official.user = user

            # Handle cropped image data for the "photo" field
            cropped_data = request.POST.get("photo_cropped")
            if cropped_data:
                try:
                    format, imgstr = cropped_data.split(";base64,")
                    ext = format.split("/")[-1]
                    data = ContentFile(
                        base64.b64decode(imgstr), name=f"photo.{ext}"
                    )
                    new_official.photo = data
                except (ValueError, TypeError):
                    messages.error(request, "Invalid image data.")
                    return render(
                        request, "athletes/newAthlete.html", {"form": cform}
                    )

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

@login_required(login_url='login')
def Officials(request):

    officials = Official.objects.all()

    context = {
        "officials": officials,
    }

    return render(request, "Officials/officials.html", context)

@login_required(login_url='login')
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

@login_required(login_url='login')
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

# _+++++++++++++++++REPORTS++++++++++++++++++++++++++++++

def deleteSchool(request, id):
    school = get_object_or_404(School, id=id)

    if request.method == "POST":
        school.delete()
        return redirect(
            "schools"
        )  # Replace 'athlete_list' with the name of your list view or any other view

    context = {
        "school": school,
    }

    return render(request, "school/deleteschool.html", context)



from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse
from django.contrib.staticfiles import finders
import base64
import os
from django.core.files.storage import default_storage
from .filters import *
from django.conf import settings

@login_required(login_url='login')
def athletesReports(request):
    # Get all athletes
    athletes = Athlete.objects.all()

    # Apply the filter
    athlete_filter = athleteFilter(request.GET, queryset=athletes)
    filtered_athletes = athlete_filter.qs

    if request.method == "POST":
        # Check which form was submitted
        if "Accreditation" in request.POST:
            template = get_template("reports/athletes/accreditation.html")
            filename = "Filtered_Accreditation.pdf"
        elif "Certificate" in request.POST:
            template = get_template(
                "reports/athletes/certificate.html"
            )  # Your certificate template
            filename = "Filtered_Certificate.pdf"
        else:
            return HttpResponse("Invalid form submission")

        # Generate PDF
        context = {"athletes": filtered_athletes,  "MEDIA_URL": settings.MEDIA_URL,}
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
        return render(request, "reports/athletes/AthletesReport.html", {"filter": athlete_filter})



# Officials Reports
@login_required(login_url='login')
def officialsReports(request):
    # Get all officials
    officials = Official.objects.all()

    # Apply the filter
    official_filter = officialFilter(request.GET, queryset=officials)
    filtered_officials = official_filter.qs

    if request.method == "POST":
        # Check which form was submitted
        if "Accreditation" in request.POST:
            template = get_template("reports/officials/accreditation.html")
            filename = "Filtered_Accreditation.pdf"
        elif "Certificate" in request.POST:
            template = get_template(
                "reports/officials/certificate.html"
            )  # Your certificate template
            filename = "Filtered_Certificate.pdf"
        else:
            return HttpResponse("Invalid form submission")

        # Generate PDF
        context = {"officials": filtered_officials}
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
        return render(request, "reports/officials/AthletesReport.html", {"filter": official_filter})


import csv
from django.http import HttpResponse


def export_acsv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="athletes.csv"'

    # Create a CSV writer object using the HttpResponse as the file.
    writer = csv.writer(response)

    # Write the header row
    writer.writerow(
        [
            "id",
            "first_name",
            "last_name",
            "school",
            "classroom",
            "gender",
            "sport",
            "country",
        ]
    )  # Replace with your model's fields

    # Write data rows
    for obj in Athlete  .objects.all():
        writer.writerow(
            [
                obj.id,
                obj.fname,
                obj.lname,
                obj.school,
                obj.classroom,
                obj.gender,
                obj.sport,
                obj.school.country,
        
            ]
        )  # Replace with your model's fields

    return response


def export_scsv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="schools.csv"'

    # Create a CSV writer object using the HttpResponse as the file.
    writer = csv.writer(response)

    # Write the header row
    writer.writerow(
        [
            "id",
            "name",
            "country",
        ]
    )  # Replace with your model's fields

    # Write data rows
    for obj in School.objects.all():
        writer.writerow(
            [
                obj.id,
                obj.name,
                obj.country,
        
            ]
        )  # Replace with your model's fields

    return response



def export_ocsv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="officials.csv"'

    # Create a CSV writer object using the HttpResponse as the file.
    writer = csv.writer(response)

    # Write the header row
    writer.writerow(
        [
            "id",
            "fname",
            "lname",
            "school",
            "gender",
            "role",
            "country",
        ]
    )  # Replace with your model's fields

    # Write data rows
    for obj in Official.objects.all():
        writer.writerow(
            [
                obj.id,
                obj.fname,
                obj.lname,
                obj.school,
                obj.gender,
                obj.role,
                obj.school.country,
        
            ]
        )  # Replace with your model's fields

    return response

def manage_positions(request):
    if request.method == 'POST':
        formset = PositionFormSet(request.POST)
        if formset.is_valid():
            try:
                formset.save()
                return redirect('register_position')
            except ValueError as e:
                formset.non_form_errors = str(e)  # Add error to formset
    else:
        # Show empty form + existing records (for display/deletion only)
        formset = PositionFormSet(
    queryset=Position.objects.all().order_by("-id")[:5]
)


    return render(request, "position/register_position.html", {"formset": formset})