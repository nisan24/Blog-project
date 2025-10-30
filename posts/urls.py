from django.urls import path
from .import views

urlpatterns = [
    path("post/", views.post_add, name="post_add"),
    path("edit/<int:id>/", views.post_edit, name="post_edit"),
    path("delete/<int:id>/", views.post_delete, name="post_delete"),
]
