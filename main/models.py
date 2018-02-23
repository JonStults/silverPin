from __future__ import unicode_literals
# from PIL import Image

from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    url = models.TextField(max_length=500, null=True)

class Machine(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    width = models.IntegerField(default=0, blank=True, null=True)
    height = models.IntegerField(default=0, blank=True, null=True)
    image = models.ImageField(null=True, blank=True, width_field="width", height_field="height")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class Tourney(models.Model):
    name = models.CharField(max_length=200)
    machine = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=300)

class HighScore(models.Model):
    first = models.CharField(max_length=50)
    second = models.CharField(max_length=50)
    third = models.CharField(max_length=50)
    machine = models.CharField(null=True, blank=True, max_length=100)

class Oldie(models.Model):
    title = models.CharField(max_length=50)
    
class OldiePic(models.Model):
    width = models.IntegerField(default=0, blank=True, null=True)
    height = models.IntegerField(default=0, blank=True, null=True)
    image = models.ImageField(null=True, blank=True, width_field="width", height_field="height")
    oldie = models.ForeignKey(Oldie, on_delete=models.CASCADE)


# class Photo(models.Model):
#     title = models.CharField(max_length=200)
#     width = models.IntegerField(default=0)
#     height = models.IntegerField(default=0)
#     image = models.ImageField(null=False, blank=False, width_field="width", height_field="height")
#     timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#
#     def __unicode__(self):
#         return self.title
#
#     class Meta:
#         ordering = ["-timestamp"]
