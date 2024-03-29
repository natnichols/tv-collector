# imports
from django.forms import BaseModelForm
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import Show, Photo, Episode
from .forms import EpisodeForm
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'nn-tv-collector'

# views
def about(request):
  return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('show-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

@login_required
def show_index(request):
  shows = Show.objects.filter(user=request.user)
  return render(request, 'shows/index.html', { 'shows': shows })

@login_required
def show_detail(request, show_id):
  show = Show.objects.get(id=show_id)
  # episode_form = EpisodeForm()
  return render(request, 'shows/detail.html', {
    'show': show, #'episode_form': episode_form
  })

# @login_required
# def add_episode(request, show_id):
#   form = EpisodeForm(request.POST)
#   if form.is_valid():
#     new_episode = form.save(commit=False)
#     new_episode.show_id = show_id
#     new_episode.save()
#   return redirect('show-detail', show_id=show_id)

@login_required
def add_photo(request, show_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, show_id=show_id)
      show_photo = Photo.objects.filter(show_id=show_id)
      if show_photo.first():
        show_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('show-detail', show_id=show_id)

class Home(LoginView):
  template_name = 'home.html'

class ShowCreate(LoginRequiredMixin, CreateView):
  model = Show
  fields = ['name', 'release_year', 'streamer', 'description']
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ShowUpdate(LoginRequiredMixin, UpdateView):
  model = Show
  fields = ['release_year', 'streamer', 'description']

class ShowDelete(LoginRequiredMixin, DeleteView):
  model = Show
  success_url = '/shows/'

class AddEpisode(LoginRequiredMixin, CreateView):
  model = Episode
  fields = '__all__'
  success_url = '/shows/'

  def get_form(self, form_class=None):
    form = super().get_form(form_class)
    form.fields['show'].queryset = form.fields['show'].queryset.filter(user=self.request.user)
    return form