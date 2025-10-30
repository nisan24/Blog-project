from django.shortcuts import render
from posts.models import PostModel

def home_view(req):
    data = PostModel.objects.all()
    print(data)
    return render(req, "home.html", {"data": data})