from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

app_name = "Main"

urlpatterns = [
    path("", views.MiLoginView.as_view(), name="login"),
    path("index/", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("logout/", LogoutView.as_view(template_name="Main/logout.html"), name="logout"),
    path("register/", views.MiRegisterView.as_view(), name="register"),
]