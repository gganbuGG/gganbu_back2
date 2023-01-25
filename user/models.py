from django.db import models

class user(models.Model):
    name=models.CharField(max_length=15,unique=True)
    puuid=models.CharField(max_length=78)
    level=models.IntegerField()
    
class match(models.Model):
    name=models.ForeignKey("user",on_delete=models.CASCADE)
    matchid=models.CharField(max_length=30)
    rank=models.IntegerField()
    petID=models.JSONField(max_length=40)
    game_level=models.IntegerField()
    traits=models.JSONField()
    augments=models.JSONField()
    units=models.JSONField()
    participant1=models.CharField(max_length=20)
    participant2=models.CharField(max_length=20)
    participant3=models.CharField(max_length=20)
    participant4=models.CharField(max_length=20)
    participant5=models.CharField(max_length=20)
    participant6=models.CharField(max_length=20)
    participant7=models.CharField(max_length=20)
    participant8=models.CharField(max_length=20)