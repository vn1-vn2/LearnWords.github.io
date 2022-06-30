from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:lesson.id>", views.lesson_intro, name="lesson_intro"),
]