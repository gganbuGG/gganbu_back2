from rest_framework import serializers
from .models import user,match

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields=['name','puuid','level']

class matchSerializer(serializers.ModelSerializer):
    class Meta:
        model=match
        fields=['name','matchid','rank','petID','game_level','traits','augments','units','participant1','participant2','participant3','participant4','participant5','participant6','participant7','participant8']