from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Dictionary, Lessons

# Create your views here.

def index(request):
    lesson = Lessons.objects.all().values()
    template = loader.get_template("index.html")
    context = {
        "lesson": lesson,
        
    }
    return HttpResponse(template.render(context, request))


def lesson(request, lesson_id):
    lesson = Lessons.objects.get(pk=lesson_id)
    template = loader.get_template("learn/lesson.html")
    context = {
        "lesson": lesson,
    }
    return HttpResponse(template.render(context, request))


def reading(request, lesson_id):
    lesson = Lessons.objects.get(pk=lesson_id)
    title = 
    template = loader.get_template("learn/reading.html")
    context = {
        "lesson": lesson,
    }
    return HttpResponse(template.render(context, request))


def exercise1(request):
    dictionary = Dictionary.objects.all().values()
    template = loader.get_template("learn/exercise1.html")
    context = {
        "dictionary": dictionary,
    }
    return HttpResponse(template.render(context, request))