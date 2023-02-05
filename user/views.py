from rest_framework import viewsets,permissions,generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
import time
import requests
import urllib.parse
from bs4 import BeautifulSoup as bs
from .models import user,match,static
from .serializers import userSerializer,matchSerializer,statSerializer


@api_view(['GET'])
def UserAPI(request):
    return Response("깐부.gg입니다.")

def getAPIkey():
    f=open("C:/devrent/back2/user/riot_api.txt","r")
    return f.read()

def Item_K(name):
    item = {
        "TFT_Item_BFSword":"BF대검",
        "TFT_Item_GargoyleStoneplate" : "가고일 돌갑옷",
        "TFT_Item_IonicSpark" : "이온충격기",
        "TFT_Item_ZekesHerald" : "지크의 전령",
        "TFT_Item_ArchangelsStaff" : "대천사의 지팡이",
        "TFT8_Item_HeartEmblemItem" : "선의 상징",
        "TFT_Item_JeweledGauntlet" : "보석 건틀릿",
        "TFT_Item_MadredsBloodrazor" : "거인학살자",
        "TFT_Item_StatikkShiv" : "스태틱의 단검",
        "TFT_Item_DragonsClaw" : "용의 발톱",
        "TFT_Item_RedBuff" : "태양불꽃 망토",
        "TFT_Item_UnstableConcoction" : "정의의 손길",
        "TFT_Item_LastWhisper" : "최후의 속삭임",
        "TFT_Item_SpearOfShojin" : "쇼진의 창",
        "TFT_Item_TitanicHydra" : "즈롯 차원문",
        "TFT_Item_GuardianAngel" : "밤의 끝자락",
        "TFT_Item_ThiefsGloves" : "도적의 장갑",
        "TFT_Item_PowerGauntlet" : "방패파괴자",
        "TFT_Item_FrozenHeart" : "수호자의 맹세",
        "TFT_Item_LocketOfTheIronSolari" : "강철의 솔라리 펜던트",
        "TFT_Item_Redemption" : "구원",
        "TFT_Item_RunaansHurricane" : "루난의 허리케인",
        "TFT8_Item_DuelistEmblemItem" : "결투가 상징",
        "TFT_Item_SeraphsEmbrace" : "푸른 파수꾼",
        "TFT_Item_HextechGunblade" : "마법공학 총검",
        "TFT_Item_Zephyr" : "서풍",
        "TFT8_Item_AnimaSquadEmblemItem" : "동물특공대 상징",
        "TFT_Item_BrambleVest" : "덤불조끼",
        "TFT8_Item_InterPolarisEmblemItem" : "레이저단 상징",
        "TFT8_Item_OxForceEmblemItem" : "황소부대 상징",
        "TFT_Item_GuinsoosRageblade" : "구인수의 격노검",
        "TFT_Item_InfinityEdge" : "무한의 대검",
        "TFT_Item_TitansResolve" : "거인의 결의",
        "TFT8_Item_DefenderEmblemItem" : "엄호대 상징",
        "TFT_Item_Bloodthirster" : "피바라기",
        "TFT4_Item_OrnnEternalWinter" : "영원한 겨울",
        "TFT_Item_WarmogsArmor" : "워모그의 갑옷",
        "TFT_Item_RabadonsDeathcap" : "라바돈의 죽음모자",
        "TFT_Item_Morellonomicon" : "모렐로노미콘",
        "TFT8_Item_RenegadeEmblemItem" : "무법자 상징",
        "TFT8_Item_AceEmblemItem" : "에이스 상징",
        "TFT8_Item_BrawlerEmblemItem" : "싸움꾼 상징",
        "TFT_Item_Chalice" : "힘의 성배",
        "TFT8_Item_CivilianEmblemItem" : "민간인 상징",
        "TFT4_Item_OrnnAnimaVisage" : "영혼의 형상",
        "TFT8_Item_ExoPrimeEmblemItem" : "메카: 프라임 상징",
        "TFT4_Item_OrnnMuramana" : "마나자네",
        "TFT_Item_Quicksilver" : "수은",
        "TFT_Item_RapidFireCannon" : "고속 연사포",
        "TFT_Item_Shroud" : "침묵의 장막",
        "TFT_Item_Deathblade" : "죽음의 검",
        "TFT8_Item_MascotEmblemItem" : "마스코트 상징",
        "TFT8_Item_DeadeyeEmblemItem" : "특등사수 상징",
        "TFT4_Item_OrnnRocketPropelledFist" : "로켓 주먹",
        "TFT8_Item_AegisEmblemItem" : "방패대 상징",
        "TFT8_Item_ReconEmblemItem" : "정찰단 상징",
        "TFT_Item_ForceOfNature" : "전략가의 왕관",
        "TFT8_Item_ADMINEmblemItem" : "자동방어체계 상징"
    }
    return item[name]

def champ_K(name):
    champ = {
    "TFT8_Kaisa" : "카이사",
    "TFT8_Lux" : "럭스",
    "TFT8_Kayle" : "케일",
    "TFT8_Poppy" : "뽀삐",
    "TFT8_Galio" : "갈리오",
    "TFT8_Rell" : "렐",
    "TFT8_Velkoz" : "벨코즈",
    "TFT8_Nilah" : "닐라",
    "TFT8_Ashe" : "애쉬",
    "TFT8_Yasuo" : "야스오",
    "TFT8_Senna" : "세나",
    "TFT8_Zed" : "제드",
    "TFT8_Lulu" : "룰루",
    "TFT8_Nunu" : "누누",
    "TFT8_Yuumi" : "유미",
    "TFT8_Zoe" : "조이",
    "TFT8_Taliyah" : "탈리야",
    "TFT8_Sivir" : "시비르",
    "TFT8_Gangplank" : "갱플랭크",
    "TFT8_WuKong" : "오공",
    "TFT8_Draven" : "드레이븐",
    "TFT8_Malphite" : "말파이트",
    "TFT8_Nasus" : "나서스",
    "TFT8_Jinx" : "징크스",
    "TFT8_Vayne" : "베인",
    "TFT8_MissFortune" : "미스포츈",
    "TFT8_Chogath" : "초가스",
    "TFT8_Rammus" : "람머스",
    "TFT8_BelVeth" : "벨베스",
    "TFT8_AurelionSol" : "아우렐리온솔",
    "TFT8_Zac" : "자크",
    "TFT8_Mordekaiser" : "모데카이저",
    "TFT8_Leblanc" : "르블랑",
    "TFT8_Sylas" : "사일러스",
    "TFT8_Camille" : "카밀",
    "TFT8_Ezreal" : "이즈리얼",
    "TFT8_Sona" : "소나",
    "TFT8_Ekko" : "에코",
    "TFT8_Sett" : "세트",
    "TFT8_Janna" : "잔나",
    "TFT8_Urgot" : "우르곳",
    "TFT8_Syndra" : "신드라",
    "TFT8_Fiddlesticks" : "피들스틱",
    "TFT8_Blitzcrank" : "블리츠크랭크",
    "TFT8_Renekton" : "레넥톤",
    "TFT8_Vi" : "바이",
    "TFT8_LeeSin" : "리신",
    "TFT8_Riven" : "리븐",
    "TFT8_Jax" : "잭스",
    "TFT8_Sejuani" : "세주아니",
    "TFT8_Soraka" : "소라카",
    "TFT8_Talon" : "탈론",
    "TFT8_Fiora" : "피오라",
    "TFT8_Annie" : "애니",
    "TFT8_Alistar" : "알리스타",
    "TFT8_Viego" : "비에고",
    "TFT8_Samira" : "사미라",
    "TFT8_Aphelios" : "아펠리오스",
    "TFT8_Leona" : "레오나"
    }

    return champ[name]

def Aug_K(name):
    augments = {
    "TFT8_Augment_StarGuardianTrait" : "별 수호자 심장",
    "TFT8_Augment_RellSupport" : "변화의 철마술",
    "TFT7_Augment_AxiomArc2" : "원칙의 원형낫2",
    "TFT7_Augment_AxiomArc1" : "원칙의 원형낫1",
    "TFT8_Augment_HackerTrait" : "해커 심장",
    "TFT8_Augment_YasuoCarry" : "흡수의 바람",
    "TFT8_Augment_InterPolarisEmblem" : "레이저단 문장",
    "TFT7_Augment_PandorasBench" : "판도라의 대기석",
    "TFT8_Augment_SonaExile" : "전력망",
    "TFT6_Augment_Diversify2" : "단결된 의지2",
    "TFT6_Augment_Diversify1" : "단결된 의지1",
    "TFT6_Augment_CelestialBlessing1" : "천상의 축복1",
    "TFT8_Augment_JinxCarry" : "신난다!",
    "TFT6_Augment_PortableForge" : "휴대용 대장간",
    "TFT6_Augment_Battlemage1" : "전투 마법사1",
    "TFT6_Augment_Battlemage2" : "전투 마법사2",
    "TFT8_Augment_JaxASCarry" : "가차없는 맹공",
    "TFT8_Augment_ExoPrimeEmblem" : "메카: 프라임 문장",
    "TFT6_Augment_ThrillOfTheHunt1" : "사냥의 전율1",
    "TFT6_Augment_ThrillOfTheHunt2" : "사냥의 전율2",
    "TFT8_Augment_JaxSupport" : "회피",
    "TFT6_Augment_SunfireBoard" : "태양불꽃판",
    "TFT8_Augment_ReconTrait" : "정찰단 심장",
    "TFT8_Augment_EzrealSupport" : "도굴꾼의 전리품",
    "TFT6_Augment_ComponentGrabBag" : "재료 꾸러미",
    "TFT8_Augment_OxForceTrait" : "황소부대 심장",
    "TFT8_Augment_OxForceEmblem" : "황소부대 문장",
    "TFT8_Augment_AnnieSupport" : "불타는 영혼",
    "TFT8_Augment_RenegadeEmblem" : "무법자 문장",
    "TFT6_Augment_CelestialBlessing2" : "천상의 축복2",
    "TFT7_Augment_Preparation2" : "준비2",
    "TFT7_Augment_Preparation1" : "준비1",
    "TFT8_Augment_LeonaSupport" : "절정의 일식",
    "TFT6_Augment_TradeSector" : "교환의 장",
    "TFT7_Augment_BigFriend2" : "커다란 친구2",
    "TFT8_Augment_MordekaiserSupport" : "말살",
    "TFT6_Augment_TomeOfTraits1" : "고대의 기록 보관소1",
    "TFT6_Augment_TomeOfTraits2" : "고대의 기록 보관소2",
    "TFT6_Augment_Featherweights2" : "경량급2",
    "TFT6_Augment_Featherweights1" : "경량급1",
    "TFT8_Augment_SettSupport" : "재생형 보호막",
    "TFT8_Augment_JannaCarry" : "신속한 보도",
    "TFT6_Augment_MetabolicAccelerator" : "대사 촉진제",
    "TFT6_Augment_JeweledLotus" : "보석 연꽃",
    "TFT6_Augment_SecondWind2" : "재생의 바람2",
    "TFT6_Augment_SecondWind1" : "재생의 바람1",
    "TFT8_Augment_NunuSupport" : "퍼지는 웃음",
    "TFT6_Augment_Electrocharge2" : "고전압2",
    "TFT6_Augment_Electrocharge1" : "고전압1",
    "TFT8_Augment_MissFortuneSupport" : "총알은 비를 타고",
    "TFT8_Augment_ChannelerEmblem2" : "주문투척자 왕관",
    "TFT8_Augment_LeBlancGlitch" : "조준 보정",
    "TFT6_Augment_CelestialBlessing3" : "천상의 축복3",
    "TFT8_Augment_LeBlancSupport" : "거울 환영",
    "TFT6_Augment_RichGetRicher" : "부익부",
    "TFT6_Augment_ForceOfNature" : "신병",
    "TFT8_Augment_SonaSupport" : "암류",
    "TFT6_Augment_TriForce2" : "3에 깃든 힘2",
    "TFT6_Augment_TriForce1" : "3에 깃든 힘1",
    "TFT6_Augment_VerdantVeil" : "신록의 장막",
    "TFT8_Augment_RivenSupport" : "금의 환향",
    "TFT6_Augment_ClearMind" : "맑은 정신",
    "TFT7_Augment_UrfsGrabBag2" : "우르프의 꾸러미2",
    "TFT7_Augment_UrfsGrabBag1" : "우르프의 꾸러미1",
    "TFT8_Augment_NilahSupport" : "승리의 장막",
    "TFT6_Augment_RadiantRelics" : "찬란한 유물",
    "TFT8_Augment_AnimaSquadEmblem" : "동물특공대 문장",
    "TFT6_Augment_WoodlandCharm" : "숲의 부적",
    "TFT8_Augment_VayneSupport" : "한밤의 서곡",
    "TFT8_Augment_AceEmblem" : "에이스 문장",
    "TFT8_Augment_UndergroundTheTrait2" : "지하세계 영혼",
    "TFT7_Augment_LivingForge" : "간이 대장간",
    "TFT8_Augment_SejuaniSupport" : "산산조각",
    "TFT7_Augment_LuckyGloves" : "행운의 장갑",
    "TFT8_Augment_SorakaSupport" : "업그레이드: 광란",
    "TFT6_Augment_SlowAndSteady" : "진보의 행진",
    "TFT7_Augment_BirthdayPresents" : "생일 선물",
    "TFT8_Augment_ZedSupport" : "약자 멸시",
    "TFT6_Augment_GachaAddict" : "황금 티켓",
    "TFT8_Augment_AlistarBeefUp" : "괴수",
    "TFT6_Augment_GrandGambler" : "큰손",
    "TFT6_Augment_TradeSectorPlus" : "교환의 장+",
    "TFT8_Augment_HackerEmblem" : "해커 문장",
    "TFT8_Augment_ZoeDoubleTrouble" : "이중 방울",
    "TFT6_Augment_TrueTwos" : "곱빼기",
    "TFT8_Augment_KaisaStarCrossed" : "엇갈린 별",
    "TFT6_Augment_Ascension" : "초월",
    "TFT7_Augment_ClutteredMind" : "어수선한 마음",
    "TFT8_Augment_GenAETrait" : "기계유망주 심장",
    "TFT8_Augment_VelkozFrostburn" : "동상 불태우기",
    "TFT6_Augment_RichGetRicherPlus" : "부익부+",
    "TFT8_Augment_DuelistEmblem" : "결투가 문장",
    "TFT6_Augment_ThreesCompany" : "삼총사",
    "TFT8_Augment_AnimaSquadTrait" : "동물특공대 심장",
    "TFT8_Augment_JinxSupport" : "전부 터져라!",
    "TFT8_Augment_BrawlerEmblem" : "싸움꾼 문장",
    "TFT8_Augment_BrawlerEmblem2" : "싸움꾼 왕관",
    "TFT8_Augment_FioraSupport" : "황소의 활력",
    "TFT8_Augment_ThreatMaxHealth" : "위협 레벨: 최대",
    "TFT7_Augment_BandOfThieves1" : "도둑 무리1",
    "TFT6_Augment_BandOfThieves2" : "도둑 무리2",
    "TFT6_Augment_MeleeStarBlade2" : "나이프의 날2",
    "TFT6_Augment_MeleeStarBlade1" : "나이프의 날1",
    "TFT8_Augment_DuelistTrait" : "결투가 심장",
    "TFT8_Augment_EkkoSupport" : "시공간 붕괴",
    "TFT8_Augment_CamilleSupport" : "마법공학 응징",
    "TFT8_Augment_YasuoSupport" : "추방자의 기백",
    "TFT8_Augment_KayleCarry" : "거룩한 승천",
    "TFT8_Augment_HeartEmblem" : "선의 문장",
    "TFT8_Augment_DravenSupport" : "무자비한 칼날",
    "TFT8_Augment_DravenCarry" : "드레이븐의 리그",
    "TFT6_Augment_TargetDummies" : "허수아비 전선",
    "TFT8_Augment_SylasSupport" : "페트리사이트 사슬",
    "TFT8_Augment_YuumiSupport" : "슈우우웅!",
    "TFT6_Augment_ItemGrabBag1" : "아이템 꾸러미1",
    "TFT6_Augment_ItemGrabBag2" : "아이템 꾸러미2",
    "TFT8_Augment_SyndraSupport" : "예비전력 강화",
    "TFT6_Augment_LudensEcho2" : "루덴의 메아리2",
    "TFT6_Augment_LudensEcho1" : "루덴의 메아리1",
    "TFT8_Augment_SivirCarry" : "배달 팁",
    "TFT8_Augment_KaisaCarry" : "다중 사격",
    "TFT8_Augment_ChannelerEmblem" : "주문투척자 문장",
    "TFT8_Augment_ZoeSupport" : "한숨 잘 시간",
    "TFT6_Augment_MaxLevel10" : "레벨 업!"
        }

    return augments[name]

def trait_K(name):
    traits={
        "Set8_AnimaSquad" : "동물 특공대",
        "Set8_Aegis" : "방패대",
        "Set8_Brawler" : "싸움꾼",
        "Set8_Civilian" : "민간인",
        "Set8_Duelist" :"결투가", 
        "Set8_GenAE":"기계유망주",
        "Set8_Heart" :"선의",
        "Set8_Mascot": "마스코트",
        "Set8_OxForce": "황소부대",
        "Set8_StarGuardian": "별 수호자",
        "Set8_Supers" : "우세",
        "Set8_Ace" : "에이스",
        "Set8_Defender" : "엄호대",
        "Set8_ExoPrime": "메카: 프라임",
        "Set8_SpaceCorps":"레이저단",
        "Set8_Channeler":"주문투척자",
        "Set8_Forecaster":"기상캐스터",
        "Set8_Prankster":"익살꾼",
        "Set8_Recon" :"정찰단",
        "Set8_UndergroundThe":"지하세계",
        "Set8_Deadeye":"특등사수",
        "Set8_Renegade":"무법자",
        "Set8_Corrupted":"타락",
        "Set8_Threat":"위협",
        "Set8_Arsenal":"병기고",
        "Set8_Hacker":"해커",
        "Set8_Admin":"자동방어체계",

    }
    return traits[name]


class usersAPI(APIView):
    def get(self,request,sname):
        
        matches=match.objects.filter(Name=sname)
        serializer=matchSerializer(matches,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def post(self,request,sname):
        key=getAPIkey()
        
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


        # 티어 LP 크롤링
        encode = urllib.parse.quote_plus(sname)
        a=requests.get("https://lolchess.gg/profile/kr/"+encode)
        req=a.text
        soup=bs(req,'html.parser')
        #더블업모드 티어 및 LP
        b=soup.find_all('div','tier-ranked-info__content')[1]
        if b.find('strong'):
            tier=b.find('strong').text
            tier=str(tier).strip()
            LP=b.find('span').text
            LP=LP[:-2]

        else:
            tier=b.find('span').text
            LP=0



        # 통계 모델 만들기
        stat=static(Name=name,Level=level,Tier=tier,LP=LP)
        if stat in static.objects.all():
            obj = static.objects.filter(Name=name)
            obj.delete()
        stat.save()
        


        

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
            traits={}
            augments=[]
            units=[]
            
            
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
                            # <못찾는 이름일경우 break 필요>
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
                            #활성화되어있는 특성만 뽑기
                            for j in i["traits"]:
                                if j["tier_current"]>=1:
                                    traits[trait_K(j["name"])]=j["num_units"]
                            
                            for j in i["augments"]:
                                augments.append(Aug_K(j))
                                
                            for j in i["units"]:
                                dict={}
                                dict["Champion"]=champ_K(j["character_id"])
                                item=[]
                                for k in j["itemNames"]:
                                    item.append(Item_K(k))
                                dict["items"]=item
                                dict["rarity"]=j["rarity"]
                                dict["tier"]=j["tier"]
                                units.append(dict)
                                

                    s=static.objects.get(Name=name)
                    s.Total_game+=1
                    s.sum_of_rank+=rank
                    if rank==1:
                        s.Win+=1
                        s.Top2+=1
                    elif rank==2:
                        s.Top2+=1
                    s.save()

                    mat=match(Name=name,Matchid=matchid,Rank=rank,PetID=petID,Game_level=game_level,Traits=traits,Augments=augments,Units=units,Participant1=participant1,Participant2=participant2,Participant3=participant3,Participant4=participant4,Participant5=participant5,Participant6=participant6,Participant7=participant7,Participant8=participant8)
                    mat.save()

                    
        
        matches=match.objects.filter(Name=name)
        serializer=matchSerializer(matches,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class statAPI(APIView):
    def get(self,request,sname):
        
        stat=static.objects.filter(Name=sname)
        serializer=statSerializer(stat,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

