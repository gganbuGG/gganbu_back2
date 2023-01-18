from django.db import models

class user(models.Model):
    name=models.CharField(max_length=15)
    iconid=models.IntegerField()
    puuid=models.CharField(max_length=78)
    level=models.IntegerField()
    summoner_id=models.CharField(max_length=63,default='')

class Profile(models.Model):
    name=models.CharField(max_length=15,default='') # 외부키로 변경
    tier=models.CharField(max_length=15)
    LP=models.IntegerField()
    win_rate=models.FloatField()
    win=models.IntegerField()
    lose=models.IntegerField()

class match_info(models.Model):
    # user 외부키
    matchID=models.CharField(max_length=15)
    info=models.JSONField()


class User_match(models.Model):
    placement=models.IntegerField()
    companion=models.CharField(max_length=20)
    
class partner_static(models.Model):
    companion=models.ForeignKey(User_match,on_delete=models.CASCADE)
    average_placement=models.FloatField()
    first_place=models.IntegerField()
    duo_number=models.IntegerField()
