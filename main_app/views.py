# imports
from django.shortcuts import render
from .models import Show

# views
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def show_index(request):
  shows = Show.objects.all()
  return render(request, 'shows/index.html', { 'shows': shows })

