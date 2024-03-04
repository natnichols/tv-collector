# imports
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Show
from .forms import EpisodeForm

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
  episode_form = EpisodeForm()
  return render(request, 'shows/detail.html', {
    'show': show, 'episode_form': episode_form
  })

class ShowCreate(CreateView):
  model = Show
  fields = '__all__'

class ShowUpdate(UpdateView):
  model = Show
  fields = ['release_year', 'streamer', 'description']

class ShowDelete(DeleteView):
  model = Show
  success_url = '/shows/'