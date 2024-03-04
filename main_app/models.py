# imports
from django.db import models
from django.urls import reverse

# models
class Show(models.Model):
  name = models.CharField(max_length=100)
  release_year = models.IntegerField()
  streamer = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('show-detail', kwargs={'show_id': self.id})

class Episode(models.Model):
  name = models.CharField(max_length=100)
  season = models.IntegerField()
  episode_num = models.IntegerField('Episode Number')
  date = models.DateField('Watch Date')
  # air_date = models.DateField() # icebox feature
  # description = models.TextField(max_length=250) # icebox feature
  show = models.ForeignKey(Show, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.name} (S{self.season}.E{self.episode_num}) watched on {self.date}"
  
  class Meta:
    ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=250)
  show = models.OneToOneField(Show, on_delete=models.CASCADE)

  def __str__(self):
      return f"Photo for show_id: {self.show_id} @{self.url}"
  