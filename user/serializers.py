from rest_framework import serializers
from .models import Profile,match_info

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=['name','tier','LP','win_rate','win','lose']

