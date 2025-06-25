from django.urls import path

from customer import views

app_name = "customer"

urlpatterns = [
    path("", views.home, name="home"),
    path("p/<slug:slug>", views.package_view, name="package"),
]
