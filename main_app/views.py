from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Game

# Create your views here.
def home(request):
    return HttpResponse('yo')

def about(request):
  return render(request, 'about.html')

def games_index(request):
  games = Game.objects.all()  
  return render(request, 'games/index.html', { 'games': games })

def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    return render(request, 'games/detail.html', { 'game': game })

# Creating class based views
class GameCreate(CreateView):
    model = Game
    fields = ['name','genre','system','description','year']
    success_url = '/games/'

class GameUpdate(UpdateView):
    model = Game
    fields = ['name','genre','system','description','year']

class GameDelete(DeleteView):
    model = Game
    success_url = '/games/'    