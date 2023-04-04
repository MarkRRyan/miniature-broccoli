from django.db import models

# Create your models here.
class Follower(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    blurb = models.TextField(max_length=250)
    
class Broccoli(models.Model):
    image = models.TextField(max_length=250)
    description = models.TextField(max_length=250)