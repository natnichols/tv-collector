# imports
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Show

# views
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def show_index(request):
  shows = Show.objects.all()
  return render(request, 'shows/index.html', { 'shows': shows })

def show_detail(request, show_id):
  show = Show.objects.get(id=show_id)
  return render(request, 'shows/detail.html', { 'show': show })

class ShowCreate(CreateView):
  model = Show
  fields = '__all__'
  success_url ='/shows/'