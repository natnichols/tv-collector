# imports
from django.db import models

# models
class Show(models.Model):
  name = models.CharField(max_length=100)
  release_year = models.IntegerField()
  streamer = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name