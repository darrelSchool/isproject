from django.shortcuts import redirect, render
from django.utils.text import slugify

from customer.forms import QuoteForm
from tour_operator import models


# Create your views here.
def home(request):
    packages = models.Package.objects.filter(visibility=True)[:10]
    return render(request, "index.html", {"packages": packages})


def package_view(request, slug):
    package = models.Package.objects.get(slug=slug)
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            newQuote = form.save(commit=False)
            newQuote.package = package
            newQuote.author = package.author
            newQuote.resolved = False
            newQuote.save()
            newQuote.slug = slugify(newQuote.id)
            newQuote.save()
            return render(
                request,
                "package.html",
                {"package": package, "form": form, "submitted": True},
            )
    form = QuoteForm()
    return render(
        request, "package.html", {"package": package, "form": form, "submitted": False}
    )
