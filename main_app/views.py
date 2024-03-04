# imports
from django.shortcuts import render

from django.http import HttpResponse

# temp data
class Show:
  def __init__(self, name, release_year, streamer, description):
    self.name = name
    self.release_year = release_year
    self.streamer = streamer
    self.description = description

shows = [
  Show('The X Files', 1993, 'Hulu', 'Two F.B.I. Agents, Fox Mulder the believer and Dana Scully the skeptic, investigate the strange and unexplained, while hidden forces work to impede their efforts.'),
  Show('Archer', 2009, 'Hulu', 'Covert black ops and espionage take a back seat to zany personalities and relationships between secret agents and drones.'),
  Show('Disenchantment', 2018, 'Netflix', 'Princess Tiabeanie - Bean- is annoyed at her imminent arranged marriage to Prince Merkimer. Then she meets Luci, a demon, and Elfo, an elf, and things get rather exciting, and dangerous.'),
  Show('Courage the Cowardly Dog', 1999, 'Max', 'The offbeat adventures of Courage, a cowardly dog who must overcome his own fears to heroically defend his unknowing farmer owners from all kinds of dangers, paranormal events and menaces that appear around their land.'),
  Show('Breaking Bad', 2008, 'Netflix', 'A chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine with a former student in order to secure his familys future.'),
  Show('The Thick of It', 2005, 'BritBox', 'The Minister for Social Affairs is continually harassed by Number 10s policy enforcer and dependent on his not-so-reliable team of civil servants.'),
]

# views
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

def show_index(request):
  return render(request, 'shows/index.html', { 'shows': shows })
