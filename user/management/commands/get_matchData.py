from django.core.management.base import BaseCommand, CommandError
from user.models import user,match_info,User_match,partner_static

import requests
import time
from time import sleep


def getAPIkey():
    f=open("C:/devrent/back2/user/riot_api.txt","r")
    return f.read()

def getpuuid(s_name):
    puuid=''
    obj=user.objects.get(name=s_name)
    puuid+=obj.puuid
    return puuid

def get_matchinfo(puuid,key,region='asia'):
    response_match=requests.get(f'https://{region}.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids?start=0&count=20&api_key={key}')
    
    #match id를 json으로 불러옴
    ids=response_match.json()

    for matchid in ids:
        response=requests.get(f'https://{region}.api.riotgames.com/tft/match/v1/matches/{matchid}?api_key={key}')

        if response.status_code==200:
            pass
        elif response.status_code==429:
            print('대기시간이 초과되었습니다. 잠시 기다려주세요')
            start_time = time.time()

            while True: # 429error가 끝날 때까지 무한 루프
                    if response.status_code == 429:
                        print('try 10 second wait time')
                        time.sleep(10)
                        response=requests.get(f'https://{region}.api.riotgames.com/tft/match/v1/matches/{matchid}?api_key={key}')
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
                break

        data = response.json()
        if data["info"]['tft_game_type'] == 'pairs':
            m = match_info.objects.filter(matchID = matchid)
            if not m :
                m = match_info(matchID = matchid,match_info = data)
                m.save()


class Command(BaseCommand):
    help="store 'user_match_data' in DB to use 'user'."
    def handle(self, *args, **options):
        API_KEY=getAPIkey()
        name=input('사용자 이름 넣기')
        puuid=getpuuid(name)
        get_matchinfo(puuid,API_KEY)
        
        
        



