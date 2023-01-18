from django.core.management.base import BaseCommand, CommandError
from user.models import user,Profile,match_info
import pandas as pd
import requests
import json
import time


def getAPIkey():
    f=open("C:/devrent/back2/user/riot_api.txt","r")
    return f.read()

def get_summoner_info(key,summonerName,country='kr',):
    response=requests.get(f'https://{country}.api.riotgames.com/tft/summoner/v1/summoners/by-name/{summonerName}?api_key={key}')

    if response.status_code==200: # 정상처리
        print('기다려주세요')
        pass

    elif response.status_code == 429:
            print('api cost full : infinite loop start')
            start_time = time.time()

            while True: # 429error가 끝날 때까지 무한 루프
                if response.status_code == 429:
                    print('try 10 second wait time')
                    time.sleep(10)
                    url = f'https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-name/{summonerName}?api_key={key}'
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
                    url = f'https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-name/{summonerName}?api_key={key}'
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
    name=data['name']
    iconid=data['profileIconId']
    puuid=data['puuid']
    level=data['summonerLevel']
    summoner_id=data['id']
    u=user(name=name,iconid=iconid,puuid=puuid,level=level,summoner_id=summoner_id)
    u.save() # u라는 db
    return summoner_id
    
def get_summoner_league(key,summonerid,country='kr',):
    response=requests.get(f'https://{country}.api.riotgames.com/tft/league/v1/entries/by-summoner/{summonerid}?api_key={key}')

    if response.status_code==200: # 정상처리
        print('기다려주세요')
        pass

    elif response.status_code == 429:
            print('api cost full : infinite loop start')
            start_time = time.time()

            while True: # 429error가 끝날 때까지 무한 루프
                if response.status_code == 429:
                    print('try 10 second wait time')
                    time.sleep(10)
                    url = f'https://{country}.api.riotgames.com/tft/league/v1/entries/by-summoner/{summonerid}?api_key={key}'
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
                    url = f'https://{country}.api.riotgames.com/tft/league/v1/entries/by-summoner/{summonerid}?api_key={key}'
                    response = requests.get(url)
                    print(response.status_code)

                elif response.status_code == 200: # 똑같이 response가 정상이면 loop escape
                    print('total error wait time : ', time.time() - start_time)
                    print('recovery api cost')
                    break

    elif response.status_code == 403: # api갱신이 필요
        print('you need api renewal')
        print('break')

    data1=response.json()
    name=data1[0]['summonerName']
    tier=data1[0]['tier']
    rank=data1[0]['rank']
    league_point=data1[0]['leaguePoints']
    win=data1[0]['wins']
    lose=data1[0]['losses']

    p=Profile(name=name,tier=tier+rank,LP=league_point,win_rate=win/(win+lose)*100,win=win,lose=lose)
    p.save() # u라는 db


class Command(BaseCommand):
    help="bring your summoner's information"
    def handle(self, *args, **kwargs):
        API_KEY=getAPIkey()
    
        sname=input("사용자 입력")
        id=get_summoner_info(API_KEY,sname)
        get_summoner_league(API_KEY,id)