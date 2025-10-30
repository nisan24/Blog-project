from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path("", views.home_view, name= "home"),
    path('admin/', admin.site.urls),
    path("author/", include("authors.urls")),
    path("category/", include("categorys.urls")),
    path("post/", include("posts.urls")),
    
]
