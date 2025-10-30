from django.shortcuts import render, redirect
from .forms import PostForm
from .models import PostModel
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def post_add(req):
    if req.user.is_authenticated:
        if req.method == "POST":
            form = PostForm(req.POST)
            if form.is_valid():
                form.instance.author = req.user
                form.save()
                return redirect("home")
        else:
            form = PostForm()
        return render(req, "posts/add_post.html", {"form": form})
    else:
        return redirect("login")


@login_required
def post_edit(req, id):
    post = PostModel.objects.get(pk = id)
    if req.method == "POST":
        form = PostForm(req.POST, instance= post)
        if form.is_valid():
            form.instance.author = req.user
            form.save()
            return redirect("profile")
    else:
        form = PostForm(instance= post)
    return render(req, "posts/add_post.html", {"form" : form, "type": "edit"})



def post_delete(req, id):
    post = PostModel.objects.get(pk = id).delete()
    return redirect("profile")