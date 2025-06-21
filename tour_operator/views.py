from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render

from tour_operator import models
from tour_operator.forms import AuthForm, CreateOperator, CreatePackage


def login_view(request):
    if request.user.is_authenticated:
        return redirect("tour_operator:home")
    if request.method == "POST":
        form = AuthForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("tour_operator:home")
    else:
        form = AuthForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("tour_operator:login")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("tour_operator:home")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


# Create your views here.
@login_required(login_url="/operator/login")
def home(request):
    user = models.Operator.objects.filter(user_id=request.user)
    if not user.exists():
        return redirect("tour_operator:add_details")
    packages = models.Package.objects.filter(author=user[0])
    return render(request, "home.html", {"user": user[0], "packages": packages})


@login_required(login_url="/operator/login")
def add_details(request):
    if request.method == "POST":
        form = CreateOperator(request.POST)
        if form.is_valid():
            newOperator = form.save(commit=False)
            newOperator.user_id = request.user
            newOperator.banned = False
            newOperator.save()
            return redirect("tour_operator:home")
    else:
        form = CreateOperator()
    return render(request, "add_details.html", {"form": form})


@login_required(login_url="/operator/login")
def create_package(request):
    user = models.Operator.objects.filter(user_id=request.user)
    if not user.exists():
        return redirect("tour_operator:add_details")
    if request.method == "POST":
        form = CreatePackage(request.POST)
        if form.is_valid():
            newPackage = form.save(commit=False)
            newPackage.author = user[0]
            newPackage.save()
            return redirect("tour_operator:home")
    else:
        form = CreatePackage()
    return render(request, "create_package.html", {"form": form})
