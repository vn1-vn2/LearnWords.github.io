from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lesson/", views.lesson, name="lesson"),
    path("reading/", views.reading, name="reading"),
    path("exercise1/", views.exercise1, name="exercise1"),
]