from django.forms import ModelForm
from .models import Episode

class EpisodeForm(ModelForm):
  class Meta:
    model = Episode
    fields = ['date', 'season', 'episode_num', 'name']