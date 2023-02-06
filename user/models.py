from django.db import models

class user(models.Model):
    name=models.CharField(max_length=15,unique=True,primary_key=True)
    Puuid=models.CharField(max_length=78)
    Level=models.IntegerField()
    
class match(models.Model):
    Name=models.ForeignKey("user",on_delete=models.CASCADE,db_column="name")
    Matchid=models.CharField(max_length=30)
    Rank=models.IntegerField()
    PetID=models.JSONField(max_length=40)
    Game_level=models.IntegerField()
    Traits=models.JSONField()
    Augments=models.JSONField()
    Units=models.JSONField()
    Participant1=models.CharField(max_length=25)
    Participant2=models.CharField(max_length=25)
    Participant3=models.CharField(max_length=25)
    Participant4=models.CharField(max_length=25)
    Participant5=models.CharField(max_length=25)
    Participant6=models.CharField(max_length=25)
    Participant7=models.CharField(max_length=25)
    Participant8=models.CharField(max_length=25)


class static(models.Model):
    Name=models.ForeignKey("user",on_delete=models.CASCADE)
    Level=models.IntegerField()
    Tier=models.CharField(max_length=20,default='')
    LP=models.IntegerField(default=0)
    Win=models.IntegerField(default=0)
    Top2=models.IntegerField(default=0)
    sum_of_rank=models.IntegerField(default=0)
    Total_game=models.IntegerField(default=0)
