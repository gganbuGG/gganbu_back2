from rest_framework import viewsets,permissions,generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
import time
import requests
import urllib.request
from bs4 import BeautifulSoup
from .models import user,match,static
from .serializers import userSerializer,matchSerializer


@api_view(['GET'])
def UserAPI(request):
    return Response("깐부.gg입니다.")

def getAPIkey():
    f=open("C:/devrent/back2/user/riot_api.txt","r")
    return f.read()

class usersAPI(APIView):
    def get(self,request,sname):
        matches=match.objects.filter(Name=sname)
        serializer=matchSerializer(matches,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def post(self,request,sname):
        key=getAPIkey()
        req=request.data #이름을 request
        summonername=sname
        
        response=requests.get(f'https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-name/{summonername}?api_key={key}') #데이터 불러오기

        if response.status_code==200: # 정상처리
                print('기다려주세요')
                pass

        elif response.status_code==404:#사용자 이름 못찾음
            if user.objects.filter(Name=summonername):
                obj = user.objects.filter(Name=summonername)
                obj.delete()
            return Response(status=status.HTTP_404_NOT_FOUND)


        elif response.status_code == 429:
            print('api cost full : infinite loop start')
            start_time = time.time()

            while True: # 429error가 끝날 때까지 무한 루프
                    if response.status_code == 429:
                        print('try 10 second wait time')
                        time.sleep(10)
                        url = f'https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-name/{summonername}?api_key={key}'
                        response = requests.get(url)
                        print(response.status_code)

                    elif response.status_code == 200: #다시 response 200이면 loop escape
                        print('total wait time : ', time.time() - start_time)                            
                        print('recovery api cost')
                        break

        elif response.status_code == 503: # 잠시 서비스를 이용하지 못하는 에러
                    print('service available error')
                    start_time = time.time()

                    while True:
                        if response.status_code == 503 or response.status_code == 429:

                            print('try 10 second wait time')
                            time.sleep(10)
                            url = f'https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-name/{summonername}?api_key={key}'
                            response = requests.get(url)
                            print(response.status_code)

                        elif response.status_code == 200: # 똑같이 response가 정상이면 loop escape
                            print('total error wait time : ', time.time() - start_time)
                            print('recovery api cost')
                            break

        elif response.status_code == 403: # api갱신이 필요
                print('you need api renewal')
                print('break')

        data=response.json()
        name=data["name"]
        puuid=data['puuid']
        level=data['summonerLevel']
        
        u=user(Name=name,Puuid=puuid,Level=level)# 유저 테이블에 puuid 와 이름, level저장
        if u in user.objects.all():
            obj = user.objects.filter(Name=name)
            obj.delete()
        u.save()

        #match id 가져오기
        response_match=requests.get(f'https://asia.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids?start=0&count=20&api_key={key}')
        ids=response_match.json() #match id들 가져오기
        
        #foreign key
        s_name=user.objects.filter(Puuid=puuid)
        name=s_name[0]

        #match 정보 가져오기
        for matchid in ids:
            response=requests.get(f'https://asia.api.riotgames.com/tft/match/v1/matches/{matchid}?api_key={key}')

            if response.status_code==200:
                pass
            elif response.status_code==429:
                print('대기시간이 초과되었습니다. 잠시 기다려주세요')
                start_time = time.time()

                while True: # 429error가 끝날 때까지 무한 루프
                        if response.status_code == 429:
                            print('try 10 second wait time')
                            time.sleep(10)
                            response=requests.get(f'https://asia.api.riotgames.com/tft/match/v1/matches/{matchid}?api_key={key}')
                            print(response.status_code)

                        elif response.status_code == 200: #다시 response 200이면 loop escape
                            print('total wait time : ', time.time() - start_time)
                            print('recovery api cost')
                            break
            elif response.status_code == 503: # 잠시 서비스를 이용하지 못하는 에러
                    print('service available error')
                    

            elif response.status_code == 403: # api갱신이 필요
                print('you need api renewal')
                print('break')
                    

            data = response.json()
            rank=0
            petID=''
            game_level=0
            traits=''
            augments=''
            units=''
            
            
            if data["info"]['tft_game_type'] == 'pairs':
                m = match.objects.filter(Matchid = matchid)
                if not m :
                    for i in range(len(data["metadata"]["participants"])):
                        if data["metadata"]["participants"][i] in user.objects.all():
                            obj=user.objects.filter(Puuid=data["metadata"]["participants"][i])
                            data["metadata"]["participants"][i]=obj["Name"]
                        else:
                            PUUID=data["metadata"]["participants"][i]
                            response=requests.get(f'https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-puuid/{PUUID}?api_key={key}')
                            namedata=response.json()
                            nickname=namedata["name"]
                            playerpuuid=namedata['puuid']
                            level=namedata['summonerLevel']
                            u=user(Name=nickname,Puuid=playerpuuid,Level=level)# 유저 테이블에 puuid 와 이름, level저장
                            u.save()
                            data["metadata"]["participants"][i]=nickname

                    participant1=data["metadata"]["participants"][0]
                    participant2=data["metadata"]["participants"][1]
                    participant3=data["metadata"]["participants"][2]
                    participant4=data["metadata"]["participants"][3]
                    participant5=data["metadata"]["participants"][4]
                    participant6=data["metadata"]["participants"][5]
                    participant7=data["metadata"]["participants"][6]
                    participant8=data["metadata"]["participants"][7]
                    
                    for i in data["info"]['participants']:
                        if puuid == i["puuid"]:
                            if i['placement']<3:
                                rank=1
                            elif i['placement']<5:
                                rank=2
                            elif i['placement']<7:
                                rank=3
                            else:
                                rank=4
                            petID=i["companion"]['content_ID']
                            game_level=i['level']
                            traits=i["traits"]
                            augments=i["augments"]
                            units=i["units"]

                        
                
                    mat=match(Name=name,Matchid=matchid,Rank=rank,PetID=petID,Game_level=game_level,Traits=traits,Augments=augments,Units=units,Participant1=participant1,Participant2=participant2,Participant3=participant3,Participant4=participant4,Participant5=participant5,Participant6=participant6,Participant7=participant7,Participant8=participant8)
                    mat.save()
        
        matches=match.objects.filter(Name=name)
        serializer=matchSerializer(matches,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

