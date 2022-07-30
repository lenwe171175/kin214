from django.contrib.gis.db import models
from django.contrib.gis.db.models import PointField

# Create your models here.

class Position(models.Model):
    userid=models.IntegerField()
    description = models.CharField(max_length=200)
    location = PointField()