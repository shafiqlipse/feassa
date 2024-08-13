from .forms import *
from .models import *
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from accounts.decorators import school_required, anonymous_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm


@anonymous_required
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect("dashboard")  # Adjust the URL name for your dashboard view
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "accounts/login.html")


def user_logout(request):
    # if user.is_authenticated:
    logout(request)
    return redirect("login")


def custom_404(request, exception):
    return render(request, "account/custom404.html", {}, status=404)


import base64
from django.core.files.base import ContentFile


def offShore(request):
    if request.method == "POST":
        cform = NocForm(request.POST, request.FILES)

        if cform.is_valid():
            new_athlete = cform.save(commit=False)

            # Handle the cropped image

            new_athlete.save()
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

    return render(request, "noc/nocregistration.html", context)


def offShare(request, id):
    noc = NOC.objects.get(id=id)

    context = {
        "noc": noc,
    }

    return render(request, "noc/officw.html", context)


from django.shortcuts import render
import base64
import os
from django.http import HttpResponse
from django.template.loader import get_template
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from dashboard.filters import *
from xhtml2pdf import pisa
from io import BytesIO


def nOfficials(request):
    # Get all officials
    nofficials = NOC.objects.all()

    # Apply the filter
    official_filter = nocFilter(request.GET, queryset=nofficials)
    filtered_officials = official_filter.qs

    if request.method == "POST":
        # Check which form was submitted
        if "Accreditation" in request.POST:
            template = get_template("noc/accreditation.html")
            filename = "Filtered_Accreditation.pdf"
        elif "Certificate" in request.POST:
            template = get_template("teams/offcert.html")  # Your certificate template
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
        return render(request, "noc/noffs.html", {"filter": official_filter})
