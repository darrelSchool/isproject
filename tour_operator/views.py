from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.text import slugify

from tour_operator import models
from tour_operator.forms import AuthForm, CreateOperator, CreatePackage, ModifyPackage


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
    count = models.Package.objects.filter(author=user[0]).count()
    active = (
        models.Package.objects.filter(author=user[0]).filter(visibility=True).count()
    )
    return render(
        request, "dash_home.html", {"user": user[0], "count": count, "active": active}
    )


@login_required(login_url="/operator/login")
def view_packages(request):
    user = models.Operator.objects.filter(user_id=request.user)
    if not user.exists():
        return redirect("tour_operator:add_details")
    packages = models.Package.objects.filter(author=user[0])
    return render(
        request,
        "dash_packages.html",
        {"user": user[0], "packages": packages, "count": packages.count()},
    )


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
        form = CreatePackage(request.POST, request.FILES)
        if form.is_valid():
            newPackage = form.save(commit=False)
            newPackage.author = user[0]
            newPackage.slug = slugify(newPackage.id)
            newPackage.save()
            return redirect("tour_operator:home")
    else:
        form = CreatePackage()
    return render(request, "dash_create.html", {"form": form})


@login_required(login_url="/operator/login")
def modify_package(request, slug):
    user = models.Operator.objects.filter(user_id=request.user)
    if not user.exists():
        return redirect("tour_operator:add_details")
    pack = models.Package.objects.get(slug=slug)
    if request.method == "POST":
        form = ModifyPackage(request.POST, request.FILES, instance=pack)
        if form.is_valid():
            form.save()
            return redirect("tour_operator:home")
    else:
        form = ModifyPackage(instance=pack)
    return render(request, "modify_package.html", {"form": form, "slug": slug})


@login_required(login_url="/operator/login")
def delete_package(request, slug):
    user = models.Operator.objects.filter(user_id=request.user)
    if not user.exists():
        return redirect("tour_operator:add_details")
    pack = models.Package.objects.get(slug=slug)
    pack.delete()
    return redirect("tour_operator:home")
