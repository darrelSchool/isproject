from django.urls import path

from customer import views

app_name = "customer"

urlpatterns = [
    path("", views.home, name="home"),
    path("search", views.search, name="search"),
    path("p/<slug:slug>", views.package_view, name="package"),
    path("a/<slug:slug>", views.add_review, name="add_review"),
]
