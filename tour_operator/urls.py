from django.urls import path

from tour_operator import views

app_name = "tour_operator"

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("add_details", views.add_details, name="add_details"),
    path("create_package", views.create_package, name="create_package"),
    path("packages", views.view_packages, name="view_packages"),
    path("quotes", views.view_quotes, name="view_quotes"),
    path("modify_package/<slug:slug>", views.modify_package, name="modify_package"),
    path("delete_package/<slug:slug>", views.delete_package, name="delete_package"),
]
