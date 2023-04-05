from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Follower(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    blurb = models.TextField(max_length=250)
    
class Broccoli(models.Model):
    image = models.TextField(max_length=250)
    description = models.TextField(max_length=250)
    
class Testimonial(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)