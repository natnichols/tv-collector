# imports
from django.urls import path
from . import views

# routes
urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('shows/', views.show_index, name='show-index'),
  path('shows/<int:show_id>/', views.show_detail, name='show-detail'),
  path('shows/create/', views.ShowCreate.as_view(), name='show-create'),
  path('shows/<int:pk>/update/', views.ShowUpdate.as_view(), name='show-update'),
  path('shows/<int:pk>/delete/', views.ShowDelete.as_view(), name='show-delete'),
]
