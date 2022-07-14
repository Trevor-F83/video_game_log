from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game, Photo

import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'video-game-log'
# Create your views here.


def home(request):
    return HttpResponse('yo')


def about(request):
    return render(request, 'about.html')


def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {'games': games})


def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    return render(request, 'games/detail.html', {'game': game})

# if slice error occurs, it is here in the key = ...
def add_photo(request, game_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, game_id=game_id)
            photo.save()
        except:
            print("Photo did not upload")
            return redirect('detail', game_id=game_id)
        return redirect('detail', game_id=game_id)
    # Creating class based views


class GameCreate(CreateView):
    model = Game
    fields = ['name', 'genre', 'system', 'description', 'year']
    success_url = '/games/'


class GameUpdate(UpdateView):
    model = Game
    fields = ['name', 'genre', 'system', 'description', 'year']


class GameDelete(DeleteView):
    model = Game
    success_url = '/games/'
