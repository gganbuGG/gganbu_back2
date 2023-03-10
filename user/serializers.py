from rest_framework import serializers
from .models import user,match,static,state

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields=['name','Level','profile_img']

class matchSerializer(serializers.ModelSerializer):
    class Meta:
        model=match
        fields=['Name','Matchid','Rank','PetID','Pet_Img','Game_level','Traits','Augments','Units','Participant']

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

class stateSerializer(serializers.ModelSerializer):
    class Meta:
        model=state
        fields=['Name','updating','last_time']