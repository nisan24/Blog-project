from django.urls import path
from .import views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("profile/", views.profile_view, name= "profile"),
    path("profile/edit/", views.profile_edit, name= "profile_edit"),
    path("logout/", views.logout_view, name= "logout"),
    path("pass_change/", views.pass_change, name= "pass_change"),
    path("set_pass/", views.set_pass, name= "set_pass"),
]
