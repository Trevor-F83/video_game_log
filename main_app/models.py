from django.db import models
from django.forms import IntegerField
from django.urls import reverse

# Create your models here.
class Game(models.Model):
    # def __init__(self, name, genre, system, year, description):
    name = models.CharField(max_length=150)
    genre = models.CharField(max_length=150)
    system = models.CharField(max_length=150)
    description = models.TextField(max_length=250)
    year = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for game_id: {self.game_id} @{self.url}"        

# games = [
#     Game('Red Dead Redemption 2', 'Action/Adventure', 'PS4', '2018', 'fun'),
#     Game('Battlefield 4','Shooter', 'PS4','2013', 'fun'),
#     Game('Elite Dangerous','Space Adventure','PS4','2014', 'fun'),
#     Game('Dirt4','Racing Sim','PS4','2017', 'fun'),
# ]