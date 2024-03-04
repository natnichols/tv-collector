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
      return reverse('show-detail', kwargs={"show_id": self.id})
  