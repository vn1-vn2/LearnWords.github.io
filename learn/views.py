from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Lessons, Dictionary


# Create your views here.
def index(request):
    index = Lessons.objects.all().values()
    template = loader.get_template("learn/index.html")
    context = {
        "index": index,
    }
    return HttpResponse(template.render(context, request))

    
def intro(request, id):
    lesson = Lessons.objects.get(id=id)
    list = Dictionary.objects.filter(id__gte=id*20-19, id__lte=id*20)
    template = loader.get_template("learn/intro.html")
    context = {
        "lesson": lesson,
        "list": list,
    }
    return HttpResponse(template.render(context, request))


def words(request, id):
    lesson = Lessons.objects.get(id=id)
    list = Dictionary.objects.filter(id__gte=id*20-19, id__lte=id*20)
    template = loader.get_template("learn/words.html")
    context = {
        "lesson": lesson,
        "list": list,
    }
    return HttpResponse(template.render(context, request))


def reading(request, id):
    lesson = Lessons.objects.get(id=id)
    template = loader.get_template("learn/reading.html")
    context = {
        "lesson": lesson,
    }
    return HttpResponse(template.render(context, request))


def exercise_a(request, id):
    lesson = Lessons.objects.get(id=id)
    list = Dictionary.objects.filter(id__gte=id*20-19, id__lte=id*20)
    template = loader.get_template("learn/exercise_a.html")
    context = {
        "lesson": lesson,
        "list": list,
    }
    return HttpResponse(template.render(context, request))