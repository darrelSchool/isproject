from django.urls import path

from tour_operator import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("add_details", views.add_details, name="add_details"),
    path("create_package", views.create_package, name="create_package"),
]
