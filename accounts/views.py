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
            cropped_image_data = request.POST.get("croppedImage")
            if cropped_image_data:
                format, imgstr = cropped_image_data.split(";base64,")
                ext = format.split("/")[-1]
                image_data = base64.b64decode(imgstr)
                new_athlete.photo = ContentFile(
                    image_data, name=f"athlete_{new_athlete.id}.{ext}"
                )

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
