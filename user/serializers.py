from rest_framework import serializers
from .models import user,match

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields=['name','puuid','level']

class matchSerializer(serializers.ModelSerializer):
    class Meta:
        model=match
        fields=['Name','Matchid','Rank','PetID','Game_level','Traits','Augments','Units','Participant1','Participant2','Participant3','Participant4','Participant5','Participant6','Participant7','Participant8']