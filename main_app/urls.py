# imports
from django.urls import path
from . import views

# routes
urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('shows/', views.show_index, name='show-index'),
  path('shows/<int:show_id>/', views.show_detail, name='show-detail'),
]
