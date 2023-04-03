from django.shortcuts import render

followers = [
  {'name': 'Mark', 'age': 32, 'blurb': 'I LOVE THE MINIATURE BROCCOLI! MINIATURE BROCCOLI IS LIFE' },
  {'name': 'Alec', 'age': 26, 'blurb': 'THE MINIATURE BROCCOLI CURED ME OF ALL MY SELF DOUBTS. THANK YOU MINIATURE BROCCOLI'},
  {'name': 'Zak', 'age': 27, 'blurb': 'THE ONLY THING I LOVE NEARLY AS MUCH AS THE MINATURE BROCCOLI IS BORGBOT, BUT MINIATURE BROCCOLI IS MY KING'}
]

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def followers_index(request):
  return render(request, 'followers/index.html', {
    'followers': followers
  })