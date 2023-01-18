from rest_framework import viewsets,permissions,generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from .models import Profile,match_info
from .serializers import ProfileSerializer

@api_view(['GET'])
def UserAPI(request):
    return Response("깐부.gg입니다.")

class ProfilesAPI(APIView):
    def get(self,request):
        profiles=Profile.objects.all()
        serializer=ProfileSerializer(profiles,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer=ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProfileAPI(APIView):
    def get(self,request,s_name):
        profile=get_object_or_404(Profile,name=s_name)
        serializer=ProfileSerializer(profile)
        return Response(serializer.data,status=status.HTTP_200_OK)

class MatchesAPI(APIView):
    def get(self,request):
        matches=match_info.objects.all()
        return Response(matches,status=status.HTTP_200_OK)

