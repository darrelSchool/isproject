from django.shortcuts import render

from tour_operator import models


# Create your views here.
def home(request):
    packages = models.Package.objects.filter(visibility=True)[:10]
    return render(request, "index.html", {"packages": packages})


def package_view(request, slug):
    package = models.Package.objects.get(slug=slug)
    return render(request, "package.html", {"package": package})
