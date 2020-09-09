from django.db import models

# Create your models here.

class Studendts(models.Model):
    name = models.CharField(max_length=10)
    adress = models.CharField(max_length=50)
    email = models.CharField(max_length=30, default='')

class scores(models.Model):
    name = models.CharField(max_length=10)
    math = models.CharField(max_length=50)
    english = models.CharField(max_length=50)
    science = models.CharField(max_length=50)