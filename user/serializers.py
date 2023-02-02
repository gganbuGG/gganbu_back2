from rest_framework import serializers
from .models import user,match,static

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields=['name','puuid','level']

class matchSerializer(serializers.ModelSerializer):
    class Meta:
        model=match
        fields=['Name','Matchid','Rank','PetID','Game_level','Traits','Augments','Units','Participant1','Participant2','Participant3','Participant4','Participant5','Participant6','Participant7','Participant8']

class statSerializer(serializers.ModelSerializer):
    Win_rate = serializers.SerializerMethodField('win_rate')
    Top2_rate = serializers.SerializerMethodField('top2_rate')
    Average_rate = serializers.SerializerMethodField('average_rank_rate')
    class Meta:
        model=static
        fields=['Name','Level','Tier','LP','Win','Win_rate','Average_rate','Top2','Top2_rate','Total_game']

    def win_rate(self,obj):
        rate= obj.Win/(obj.Total_game)
        rate=round(rate*100,2)
        return rate

    def top2_rate(self,obj):
        rate=obj.Top2 / (obj.Total_game)
        rate=round(rate*100,2)
        return rate

    def average_rank_rate(self,obj):
        rate=obj.sum_of_rank / (obj.Total_game)
        rate=round(rate,2)
        return rate

