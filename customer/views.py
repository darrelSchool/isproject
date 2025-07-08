from django.db.models import Q
from django.shortcuts import redirect, render
from django.utils.http import RFC3986_GENDELIMS
from django.utils.text import slugify

from customer.forms import QuoteForm, ReviewForm, SearchForm
from customer.models import Review
from tour_operator import models


# Create your views here.
def home(request):
    packages = models.Package.objects.filter(visibility=True)[:10]
    search_form = SearchForm()
    return render(
        request,
        "index.html",
        {"packages": packages, "search": False, "search_form": search_form},
    )


def search(request):
    if request.method == "POST":
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            search_term = request.POST["search_item"]
            packages = models.Package.objects.filter(
                Q(title__contains=search_term)
                | Q(description__contains=search_term)
                | Q(title__contains=search_term.lower())
                | Q(description__contains=search_term.lower())
            )
            search_form = SearchForm()
            return render(
                request,
                "index.html",
                {"packages": packages, "search": True, "search_form": search_form},
            )
    return redirect("customer:home")


def add_review(request, slug):
    quote_form = QuoteForm()
    package = models.Package.objects.get(slug=slug)
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            newReview = review_form.save(commit=False)
            newReview.package = package
            newReview.save()
            return render(
                request,
                "package.html",
                {
                    "package": package,
                    "form": quote_form,
                    "review_form": review_form,
                    "submitted": False,
                },
            )
    return redirect("customer:home")


def package_view(request, slug):
    package = models.Package.objects.get(slug=slug)
    reviews = Review.objects.filter(package=package)
    review_form = ReviewForm(request.POST)
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
                {
                    "package": package,
                    "reviews": reviews,
                    "form": form,
                    "review_form": review_form,
                    "submitted": True,
                },
            )
    form = QuoteForm()
    return render(
        request,
        "package.html",
        {
            "package": package,
            "reviews": reviews,
            "review_form": review_form,
            "form": form,
            "submitted": False,
        },
    )
