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


# championships
"""
def schools(request):
    schools = School.objects.all()
    new_school = None

    if request.method == "POST":
        sform = SchoolForm(request.POST, request.FILES)

        if sform.is_valid():
            new_school = sform.save(commit=False)

            new_school.save()
            return redirect("schools")
    else:
        sform = SchoolForm()
    context = {"schools": schools, "sform": sform}
    return render(request, "school/schools.html", context)

"""
# add championships

"""
def schoolDetail(request, id):
    school = School.objects.get(id=id)
    athletes = Athlete.objects.filter(school=school)
    new_athlete = None

    if request.method == "POST":
        cform = AthleteForm(request.POST, request.FILES)

        if cform.is_valid():
            new_athlete = cform.save(commit=False)
            new_athlete.school = school

            new_athlete.save()
            return redirect("schoolDetail", school.id)
    else:
        cform = AthleteForm()

    context = {
        "school": school,
        "athletes": athletes,
        "cform": cform,
    }

    return render(request, "school/school.html", context)


def AthleteDetail(request, id):
    athlete = Athlete.objects.get(id=id)

    context = {
        "athlete": athlete,
    }

    return render(request, "school/athlete.html", context)
"""
