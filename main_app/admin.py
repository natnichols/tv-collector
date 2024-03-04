# imports
from django.contrib import admin
from .models import Show, Episode

# registered models
admin.site.register(Show)
admin.site.register(Episode)