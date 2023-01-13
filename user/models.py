from django.db import models

class user(models.Model):
    name=models.CharField(max_length=15)
    iconid=models.IntegerField()
    puuid=models.CharField(max_length=78)
    level=models.IntegerField()
    summoner_id=models.CharField(max_length=63,default='')

class Profile(models.Model):
    name=models.CharField(max_length=15,default='')
    tier=models.CharField(max_length=15)
    LP=models.IntegerField()
    win_rate=models.FloatField()
    win=models.IntegerField()
    lose=models.IntegerField()