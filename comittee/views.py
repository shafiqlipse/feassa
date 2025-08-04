from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from accounts.decorators import school_required, anonymous_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.files.base import ContentFile
import base64
# Create your views here.


def committee(request):
    if request.method == "POST":
        cform = NocForm(request.POST, request.FILES)

        if cform.is_valid():
            new_comittee = cform.save(commit=False)

            # Handle the cropped image
            cropped_data = request.POST.get("photo_cropped")
            if cropped_data:
                try:
                    format, imgstr = cropped_data.split(";base64,")
                    ext = format.split("/")[-1]
                    data = ContentFile(
                        base64.b64decode(imgstr), name=f"photo.{ext}"
                    )
                    new_comittee.photo = data
                except (ValueError, TypeError):
                    messages.error(request, "Invalid image data.")
                    return render(
                        request, "comittee/addcomittee.html", {"cform": cform}
                    )
            new_comittee.save()
            messages.success(request, "Form submitted successfully.")
            return redirect("noc")
        else:
            for field, errors in cform.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        cform = NocForm()

    context = {
        "cform": cform,
    }

    return render(request, "comittee/addcomittee.html", context)

@login_required(login_url='login')
def committees(request):
    comittees = NOC.objects.all()

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

from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template
from django.http import HttpResponse
from .filters import *
import base64
from django.conf import settings
# This function is used to generate reports for comittees
@login_required(login_url='login')
def comitteesReports(request):
    # Get all comittees
    comittees = NOC.objects.all()

    # Apply the filter
    comittee_filter = comitteeFilter(request.GET, queryset=comittees)
    filtered_comittees = comittee_filter.qs

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
        return render(request, "reports/media/comitteesReport.html", {"filter": comittee_filter})

# Note: The above code assumes you have a template named "reports/media/accreditation.html"
# and "reports/media/certificate.html" for generating the respective reports.
# Adjust the template paths as necessary based on your project structure.   


# This function is used to generate reports for medias
@login_required(login_url='login')
def mediaAccreditation(request):
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
        return render(request, "reports/media/mediaReports.html", {"filter": media_filter})


def media(request):
    if request.method == "POST":
        cform = MediaForm(request.POST, request.FILES)

        if cform.is_valid():
            new_media = cform.save(commit=False)

            # Handle the cropped image
            cropped_data = request.POST.get("photo_cropped")
            if cropped_data:
                try:
                    format, imgstr = cropped_data.split(";base64,")
                    ext = format.split("/")[-1]
                    data = ContentFile(
                        base64.b64decode(imgstr), name=f"photo.{ext}"
                    )
                    new_media.photo = data
                except (ValueError, TypeError):
                    messages.error(request, "Invalid image data.")
                    return render(
                        request, "media/addmedia.html", {"cform": cform}
                    )
            new_media.save()
            messages.success(request, "Form submitted successfully.")
            return redirect("noc")
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

@login_required(login_url='login')
def mediaList(request):
    medias = Media.objects.all()

    context = {
        "medias": medias,
    }

    return render(request, "media/medias.html", context)

@login_required(login_url='login')
def mediaDetail(request, id):
    media = Media.objects.get(id=id)

    context = {
        "media": media,
    }

    return render(request, "media/media.html", context)

