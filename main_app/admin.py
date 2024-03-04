# imports
from django.contrib import admin
from .models import Show, Episode, Photo

# registered models
admin.site.register(Show)
admin.site.register(Episode)
admin.site.register(Photo)