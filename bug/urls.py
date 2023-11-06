from django.contrib import admin
from django.urls import path
from bug.views import UserApiView, BugsApiView

urlpatterns = [
    path("users/", UserApiView.as_view(), name="users-api"),
    path("bugs/", BugsApiView.as_view(), name="bugs-api"),
]
