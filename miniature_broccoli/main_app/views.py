from django.shortcuts import render, redirect
from .models import Follower, Broccoli, Testimonial
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def followers_index(request):
  followers = Follower.objects.all()
  return render(request, 'followers/index.html', { 'followers': followers })
  
def images(request):
  broccolis = Broccoli.objects.all()
  return render(request, 'images.html', {
    'broccolis': broccolis
  })
  
def testimonial(request):
  testimonials = Testimonial.objects.all()
  return render(request, 'main_app/testimonial.html', {
    'testimonials': testimonials
  })
  
  
  
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # Save the user to the db
      user = form.save()
      # Automatically log in the new user
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup template
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)