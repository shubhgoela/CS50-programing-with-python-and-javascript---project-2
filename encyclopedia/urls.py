from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.index2, name="dis"),
    path("wiki/", views.rand, name="rand"),
    path("search/", views.search, name="search"),
    path("search/<str:title>", views.err, name="searcherr"),
    path("CNP/", views.CNP, name="CNP"),
    path("CNP/<str:title>", views.err, name="CNPerr"),
    path("edit/<str:title>", views.editEntry, name="edit"),
    path("<str:title>", views.err, name="error")
]
