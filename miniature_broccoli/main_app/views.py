from django.shortcuts import render
from .models import Follower

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def followers_index(request):
  followers = Follower.objects.all()
  return render(request, 'followers/index.html', { 'followers': followers })
  
def images(request):
  return render(request, 'images.html', {
    'images': images
  })