from django.urls import path

from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("intro<int:id>", views.intro, name="intro"),
    path("words<int:id>", views.words, name="words"),
    path("reading<int:id>", views.reading, name="reading"),
    path("exercise_a<int:id>", views.exercise_a, name="exercise_a"),
]