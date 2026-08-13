from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *

from django.urls import reverse
from django.contrib.auth import login, logout
from accounts.decorators import school_required, anonymous_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.files.base import ContentFile
import base64
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template
from django.http import HttpResponse
from .filters import *
import base64
from django.conf import settings
# Create your views here.


def committee(request):
    if request.method == "POST":
        cform = NocForm(request.POST, request.FILES)

        if cform.is_valid():
            new_comittee = cform.save(commit=False)

            # Handle the cropped image

            new_comittee.save()
            messages.success(request, "Form submitted successfully.")
            return  redirect(reverse('committee_success', args=[new_comittee.id]))
        else:
            for field, errors in cform.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        cform = NocForm()

    context = {
        "cform": cform,
    }

    return render(request, "comittee/addcommittee.html", context)

def committee_success(request,id):
    committee = NOC.objects.filter(id=id).first()
    
    if not committee:
        return render(request, 'registration_failed.html', {'error': 'Journalist not registered'})

    return render(request, 'comittee/success.html', {
        'committee': committee,

    })

@login_required(login_url='login')
def all_committee_members(request):
    comittees = NOC.objects.all()

    context = {
        "comittees": comittees,
    }

    return render(request, "comittee/comittees.html", context)

@login_required(login_url='login')
def committees(request):
    country = request.user.country
    comittees = NOC.objects.filter(country = country)

    context = {
        "comittees": comittees,
    }

    return render(request, "comittee/comittees.html", context)

@login_required(login_url='login')
def committeeDetail(request, id):
    comittee = NOC.objects.get(id=id)

    context = {
        "comittee": comittee,
    }

    return render(request, "comittee/comittee.html", context)


@login_required(login_url='login')
def edit_committee(request, id):
    committee = NOC.objects.get(id=id)

    if request.method == "POST":
        cform = NocForm(request.POST, request.FILES, instance=committee)

        if cform.is_valid():
            updated_committee = cform.save(commit=False)



            updated_committee.save()
            messages.success(request, "Committee updated successfully.")
            return redirect("committees")
        else:
            for field, errors in cform.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        cform = NocForm(instance=committee)

    context = {
        "cform": cform,
        "committee": committee,
    }
    return render(request, "comittee/addcommittee.html", context)
# return render(request, "comittee/addcomittee.html", context)


@login_required(login_url='login')
def delete_committee(request, id):
    comittee = get_object_or_404(NOC, id=id)

    if request.method == "POST":
        comittee.delete()
        messages.success(request, "Committee deleted successfully.")
        return redirect("committees")  # Change to your actual list view name

    return render(request, "comittee/delete_committee.html", {"comittee": comittee})
# return render(request, "comittee/addcomittee.html", context)

# This function is used to generate reports for comittees
@login_required(login_url='login')
def comitteesReports(request):
    
    user = request.user
    country = user.country
    # Get all comittees
    comittees = NOC.objects.filter(country = country)

    # Apply the filter
    comittee_filter = comitteeFilter(request.GET, queryset=comittees)
    filtered_comittees = comittee_filter.qs

    if request.method == "POST":
        # Check which form was submitted
        if "Accreditation" in request.POST:
            template = get_template("reports/comitees/accreditation.html")
            filename = "Filtered_Accreditation.pdf"
        elif "Certificate" in request.POST:
            template = get_template(
                "reports/comitees/certificate.html"
            )  # Your certificate template
            filename = "Filtered_Certificate.pdf"
        else:
            return HttpResponse("Invalid form submission")

        # Generate PDF
        context = {"comittees": filtered_comittees,  "MEDIA_URL": settings.MEDIA_URL,}
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
        return render(request, "reports/comitees/comitteesReport.html", {"filter": comittee_filter})

# This function is used to generate reports for comittees
@login_required(login_url='login')
def all_comitteesReports(request):
    # Get all comittees
    comittees = NOC.objects.all()

    # Apply the filter
    comittee_filter = comitteeFilter(request.GET, queryset=comittees)
    filtered_comittees = comittee_filter.qs

    if request.method == "POST":
        # Check which form was submitted
        if "Accreditation" in request.POST:
            template = get_template("reports/comitees/accreditation.html")
            filename = "Filtered_Accreditation.pdf"
        elif "Certificate" in request.POST:
            template = get_template(
                "reports/comitees/certificate.html"
            )  # Your certificate template
            filename = "Filtered_Certificate.pdf"
        else:
            return HttpResponse("Invalid form submission")

        # Generate PDF
        context = {"comittees": filtered_comittees,  "MEDIA_URL": settings.MEDIA_URL,}
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
        return render(request, "reports/comitees/comitteesReport.html", {"filter": comittee_filter})

# Note: The above code assumes you have a template named "reports/media/accreditation.html"
# and "reports/media/certificate.html" for generating the respective reports.
# Adjust the template paths as necessary based on your project structure.   
# This function is used to generate reports for medias

@login_required(login_url='login')
def mediaAccreditation(request):
    # Get all medias
    country = request.user.country
  
    medias = Media.objects.filter(country = country)

    # Apply the filter
    media_filter = mediaFilter(request.GET, queryset=medias)
    filtered_medias = media_filter.qs

    if request.method == "POST":
        # Check which form was submitted
        if "Accreditation" in request.POST:
            template = get_template("reports/media/accreditation.html")
            filename = "Filtered_Accreditation.pdf"
        elif "Certificate" in request.POST:
            template = get_template(
                "reports/media/certificate.html"
            )  # Your certificate template
            filename = "Filtered_Certificate.pdf"
        else:
            return HttpResponse("Invalid form submission")

        # Generate PDF
        context = {"medias": filtered_medias,  "MEDIA_URL": settings.MEDIA_URL,}
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
        return render(request, "reports/media/mediaReport.html", {"filter": media_filter})


@login_required(login_url='login')
def all_mediaAccreditation(request):
    # Get all medias
    medias = Media.objects.all()

    # Apply the filter
    media_filter = mediaFilter(request.GET, queryset=medias)
    filtered_medias = media_filter.qs

    if request.method == "POST":
        # Check which form was submitted
        if "Accreditation" in request.POST:
            template = get_template("reports/media/accreditation.html")
            filename = "Filtered_Accreditation.pdf"
        elif "Certificate" in request.POST:
            template = get_template(
                "reports/media/certificate.html"
            )  # Your certificate template
            filename = "Filtered_Certificate.pdf"
        else:
            return HttpResponse("Invalid form submission")

        # Generate PDF
        context = {"medias": filtered_medias,  "MEDIA_URL": settings.MEDIA_URL,}
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
        return render(request, "reports/media/mediaReport.html", {"filter": media_filter})

@login_required(login_url='login')
def delete_media(request, id):
    media = get_object_or_404(Media, id=id)

    if request.method == "POST":
        media.delete()
        messages.success(request, "Media deleted successfully.")
        return redirect("media_list")  # Change to your actual list view name

    return render(request, "media/delete_media.html", {"media": media})

def media(request):
    if request.method == "POST":
        cform = MediaForm(request.POST, request.FILES)

        if cform.is_valid():
            new_media = cform.save(commit=False)

            # Handle the cropped image

            new_media.save()
            messages.success(request, "Form submitted successfully.")
            return  redirect(reverse('media_success', args=[new_media.id]))  
        else:
            for field, errors in cform.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        cform = MediaForm()

    context = {
        "cform": cform,
    }

    return render(request, "media/addmedia.html", context)


def media_success(request,id):
    media = Media.objects.filter(id=id).first()
    
    if not media:
        return render(request, 'registration_failed.html', {'error': 'Journalist not registered'})

    return render(request, 'media/success.html', {
        'media': media,

    })
    
    
@login_required(login_url='login')
def media_list(request):
    country = request.user.country
    medias = Media.objects.filter(country = country)

    context = {
        "medias": medias,
    }
    return render(request, "media/journalists.html", context)

@login_required(login_url='login')
def all_media_list(request):
    medias = Media.objects.all()

    context = {
        "medias": medias,
    }
    return render(request, "media/journalists.html", context)

@login_required(login_url='login')
def mediaDetail(request, id):
    media = Media.objects.get(id=id)

    context = {
        "media": media,
    }

    return render(request, "media/media.html", context)


# Note: The above code assumes you have a template named "reports/media/accreditation.html"
# and "reports/media/certificate.html" for generating the respective reports.
# Adjust the template paths as necessary based on your project structure.   


# This function is used to generate reports for medias
@login_required(login_url='login')
def OfficiatingOfficialsAccreditation(request):
    # Get all medias
    country = request.user.country
    match_officials = OfficiatingOfficials.objects.filter(country = country)

    # Apply the filter
    match_officials_filter = mediaFilter(request.GET, queryset=match_officials)
    filtered_match_officials = match_officials_filter.qs

    if request.method == "POST":
        # Check which form was submitted
        if "Accreditation" in request.POST:
            template = get_template("reports/match_officials/accreditation.html")
            filename = "Filtered_Accreditation.pdf"
        elif "Certificate" in request.POST:
            template = get_template(
                "reports/match_officials/certificate.html"
            )  # Your certificate template
            filename = "Filtered_Certificate.pdf"
        else:
            return HttpResponse("Invalid form submission")

        # Generate PDF
        context = {"match_officials": filtered_match_officials,  "MEDIA_URL": settings.MEDIA_URL,}
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
        return render(request, "reports/match_officials/match_officials_report.html", {"filter": match_officials_filter})
# This function is used to generate reports for medias
@login_required(login_url='login')
def all_OfficiatingOfficialsAccreditation(request):
    # Get all medias
    match_officials = OfficiatingOfficials.objects.all()

    # Apply the filter
    match_officials_filter = mediaFilter(request.GET, queryset=match_officials)
    filtered_match_officials = match_officials_filter.qs

    if request.method == "POST":
        # Check which form was submitted
        if "Accreditation" in request.POST:
            template = get_template("reports/match_officials/accreditation.html")
            filename = "Filtered_Accreditation.pdf"
        elif "Certificate" in request.POST:
            template = get_template(
                "reports/match_officials/certificate.html"
            )  # Your certificate template
            filename = "Filtered_Certificate.pdf"
        else:
            return HttpResponse("Invalid form submission")

        # Generate PDF
        context = {"match_officials": filtered_match_officials,  "MEDIA_URL": settings.MEDIA_URL,}
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
        return render(request, "reports/match_officials/match_officials_report.html", {"filter": match_officials_filter})

@login_required(login_url='login')
def delete_match_official(request, id):
    match_official = get_object_or_404(OfficiatingOfficials, id=id)

    if request.method == "POST":
        match_official.delete()
        messages.success(request, "Media deleted successfully.")
        return redirect("match_officials_list")  # Change to your actual list view name

    return render(request, "match_officials/delete_match_official.html", {"match_official": match_official})


def add_match_official(request):
    if request.method == "POST":
        cform = OfficiatingOfficialsForm(request.POST, request.FILES)

        if cform.is_valid():
            new_match_official = cform.save(commit=False)

            # Handle the cropped image

            new_match_official.save()
            messages.success(request, "Form submitted successfully.")
            return  redirect(reverse('match_official_success', args=[new_match_official.id]))  
        else:
            for field, errors in cform.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        cform = OfficiatingOfficialsForm()

    context = {
        "cform": cform,
    }

    return render(request, "match_officials/add_match_official.html", context)

def match_official_success(request,id):
    match_official = OfficiatingOfficials.objects.filter(id=id).first()
    
    if not match_official:
        return render(request, 'registration_failed.html', {'error': 'Journalist not registered'})

    return render(request, 'match_officials/success.html', {
        'match_official': match_official,

    })
   
@login_required(login_url='login')
def match_official_list(request):
    country = request.user.country
    match_officials = OfficiatingOfficials.objects.filter(country = country)

    context = {
        "match_officials": match_officials,
    }
    return render(request, "match_officials/match_official_list.html", context)

@login_required(login_url='login')
def all_match_official(request):
    match_officials = OfficiatingOfficials.objects.all()

    context = {
        "match_officials": match_officials,
    }
    return render(request, "match_officials/match_official_list.html", context)

@login_required(login_url='login')
def match_official_detail(request, id):
    match_official = OfficiatingOfficials.objects.get(id=id)

    context = {
        "match_official": match_official,
    }

    return render(request, "match_officials/match_official.html", context)

def success(request):
    return render(request, "comittee/success.html")