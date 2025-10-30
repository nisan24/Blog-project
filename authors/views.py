from django.shortcuts import render, redirect
from .forms import RegisterForm, UserChangeData
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from posts.models import PostModel
# Create your views here.

@login_required
def profile_view(req):
    data = PostModel.objects.filter(author = req.user)
    return render(req, "authors/profile.html", {"user": req.user, "data": data})



def profile_edit(req):
    if req.user.is_authenticated:
        if req.method == "POST":
            form = UserChangeData(req.POST, instance= req.user)
            if form.is_valid():
                form.save()
                return redirect("profile")
        else:
            form = UserChangeData(instance= req.user)
        return render(req, "authors/profile_edit.html", {"form": form})
    else:
        return redirect("login")


def register_view(req):
    if not req.user.is_authenticated:
        if req.method == "POST":
            form = RegisterForm(req.POST)
            if form.is_valid():
                form.save()
                return redirect("login")
        else:
            form = RegisterForm()
        return render(req, "authors/register.html", {"form": form})
    else:
        return redirect("profile")



def login_view(req):
    if not req.user.is_authenticated:
        if req.method == "POST":
            form = AuthenticationForm(request= req, data = req.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                user_pass = form.cleaned_data["password"]
                user = authenticate(username = username, password = user_pass)
                if user is not None:
                    login(req, user)
                    return redirect("profile")
        else:
            form = AuthenticationForm(request= req)
        return render(req, "authors/login.html", {"form": form})
    else:
        return redirect("profile")


def logout_view(req):
    logout(req)
    return redirect("login")


@login_required
def pass_change(req):
    if req.user.is_authenticated:
        if req.method == "POST":
            form = PasswordChangeForm(user= req.user, data = req.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(req, req.user)
                return redirect("profile")
        else:
            form = PasswordChangeForm(user= req.user)
        return render(req, "authors/pass_change.html", {"form": form})
    else:
        return redirect("login")



@login_required
def set_pass(req):
    if req.user.is_authenticated:
        if req.method == "POST":
            form = SetPasswordForm(user= req.user, data = req.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(req, req.user)
                return redirect("profile")
        else:
            form = SetPasswordForm(user= req.user)
        return render(req, "authors/pass_change.html", {"form": form, "type": "set_pass"})
    else:
        return redirect("login")
    
    
