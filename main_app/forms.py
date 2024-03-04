from django.forms import ModelForm
from .models import Episode

class EpisodeForm(ModelForm):
  class Meta:
    model = Episode
    fields = ['watch_date', 'season', 'episode_num', 'name']