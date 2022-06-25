from pyexpat import model
from django.db import models


# Create your models here.
class Dictionary(models.Model):
    word = models.CharField(max_length=20)
    definition = models.CharField(max_length=200)


class Lessons(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=10000)
