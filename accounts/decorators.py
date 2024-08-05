from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from functools import wraps

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def staff_required(view_func):
    @login_required(login_url="login")
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_games:
            return view_func(request, *args, **kwargs)
        else:
            return render(
                request, "accounts/login.html"
            )  # You can customize this template

    return _wrapped_view


def school_required(view_func):
    @login_required(login_url="login")
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_admin:
            return view_func(request, *args, **kwargs)
        else:
            return render(
                request, "accounts/login.html"
            )  # You can customize this template

    return _wrapped_view


def anonymous_required(view_func):

    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, "dashboard/home.html")  # Customize this template
        else:
            return view_func(request, *args, **kwargs)

    return _wrapped_view
