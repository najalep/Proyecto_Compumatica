from django.contrib.auth.decorators import login_required
from django.shortcuts import *
from django.utils.decorators import method_decorator


def login(request):
    return render(request, "registration/../../login/templates/login.html")


def index(request):
    return render(request, "img.html")
