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
    'TFT_Consumable_NeekosHelp': '챔피언 복제기',
    'TFT_Item_BFSword': 'B.F. 대검', 
    'TFT_Item_Bloodthirster': '피바라기', 
    'TFT_Item_BrambleVest': '덤불 조끼', 
    'TFT_Item_ChainVest': '쇠사슬 조끼', 
    'TFT_Item_SparringGloves': '연습용 장갑',
    'TFT_Item_Deathblade': '죽음의 검',
    'TFT_Item_DragonsClaw': '용의 발톱', 
    'TFT_Item_EmptyBag': '',
    'TFT_Item_ForceOfNature': '전략가의 왕관',
    'TFT_Item_ThiefsGloves': '도적의 장갑',
    'TFT_Item_ThiefsGloves_Empty': '', 
    'TFT_Item_Shroud': '침묵의 장막',
    'TFT_Item_FrozenHeart': '수호자의 맹세', 
    'TFT_Item_GiantsBelt': '거인의 허리띠', 
    'TFT_Item_MadredsBloodrazor': '거인 학살자', 
    'TFT_Item_GuardianAngel': '밤의 끝자락', 
    'TFT_Item_GuinsoosRageblade': '구인수의 격노검',
    'TFT_Item_UnstableConcoction': '정의의 손길', 
    'TFT_Item_HextechGunblade': '마법공학 총검', 
    'TFT_Item_Chalice': '힘의 성배', 
    'TFT_Item_InfinityEdge': '무한의 대검', 
    'TFT_Item_IonicSpark': '이온 충격기',
    'TFT_Item_JeweledGauntlet': '보석 건틀릿', 
    'TFT_Item_LastWhisper': '최후의 속삭임',
    'TFT_Item_LocketOfTheIronSolari': '강철의 솔라리 펜던트',
    'TFT_Item_ArchangelsStaff': '대천사의 지팡이',
    'TFT_Item_Spatula': '뒤집개', 
    'TFT_Item_Quicksilver': '수은', 
    'TFT_Item_Morellonomicon': '모렐로노미콘',
    'TFT_Item_NeedlesslyLargeRod': '쓸데없이 큰 지팡이', 
    'TFT_Item_NegatronCloak': '음전자 망토',
    'TFT_Item_PowerGauntlet': '방패파괴자', 
    'TFT_Item_RabadonsDeathcap': '라바돈의 죽음모자', 
    'TFT_Item_RapidFireCannon': '고속 연사포', 
    'TFT_Item_RecurveBow': '곡궁', 
    'TFT_Item_RedBuff': '태양불꽃 망토', 
    'TFT_Item_Redemption': '구원',
    'TFT_Item_RunaansHurricane': '루난의 허리케인', 
    'TFT_Item_SeraphsEmbrace': '푸른 파수꾼',
    'TFT_Item_SpearOfShojin': '쇼진의 창', 
    'TFT_Item_StatikkShiv': '스태틱의 단검',
    'TFT_Item_GargoyleStoneplate': '가고일 돌갑옷',
    'TFT_Item_TearOfTheGoddess': '여신의 눈물',
    'TFT_Item_TitanicHydra': '즈롯 차원문',
    'TFT_Item_TitansResolve': '거인의 결의',
    'TFT_Item_WarmogsArmor': '워모그의 갑옷',
    'TFT_Item_ZekesHerald': '지크의 전령',
    'TFT_Item_Zephyr': '서풍', 
    'TFT_Consumable_ItemRemover': '자석 제거기',
    'TFT_Consumable_ItemReroller': '재조합기', 
    'TFT_Consumable_ShopReroller': '사기 주사위', 
    'TFT4_Item_OrnnAnimaVisage': '영혼의 형상',
    'TFT4_Item_OrnnDeathsDefiance': '죽음의 저항', 
    'TFT4_Item_OrnnEternalWinter': '영원한 겨울',
    'TFT4_Item_OrnnTheCollector': '황금 징수의 총', 
    'TFT4_Item_OrnnInfinityForce': '무한한 삼위일체',
    'TFT4_Item_OrnnMuramana': '마나자네', 
    'TFT4_Item_OrnnObsidianCleaver': '흑요석 양날 도끼',
    'TFT4_Item_OrnnRanduinsSanctum': '란두인의 성소', 
    'TFT4_Item_OrnnRocketPropelledFist': '로켓 주먹', 
    'TFT4_Item_OrnnZhonyasParadox': '존야의 역설',
    'TFT5_Item_TrapClawRadiant': '의지파괴자',
    'TFT5_Item_BloodthirsterRadiant': '축복받은 피바라기',
    'TFT5_Item_BlueBuffRadiant': '푸른 축복',
    'TFT5_Item_ChaliceOfPowerRadiant': '선의의 성배', 
    'TFT5_Item_IonicSparkRadiant': '집단 충격기', 
    'TFT5_Item_GiantSlayerRadiant': '악마 학살자',
    'TFT5_Item_DragonsClawRadiant': '용의 의지',
    'TFT5_Item_GargoyleStoneplateRadiant': '수호상 돌갑옷',
    'TFT5_Item_LastWhisperRadiant': '영겁의 속삭임',
    'TFT5_Item_HandOfJusticeRadiant': '공정의 주먹',
    'TFT5_Item_FrozenHeartRadiant': '철갑의 서약',
    'TFT5_Item_JeweledGauntletRadiant': '눈부신 건틀릿', 
    'TFT5_Item_GuardianAngelRadiant': '새벽의 서광',
    'TFT5_Item_GuinsoosRagebladeRadiant': '구인수의 심판', 
    'TFT5_Item_HextechGunbladeRadiant': '마법공학 생명검',
    'TFT5_Item_LocketOfTheIronSolariRadiant': '타곤 정상의 펜던트', 
    'TFT5_Item_DeathbladeRadiant': '빛나는 죽음의 검', 
    'TFT5_Item_ZephyrRadiant': '겨울바람',
    'TFT5_Item_MorellonomiconRadiant': '엔젤로노미콘', 
    'TFT5_Item_QuicksilverRadiant': '반짝이는 수은', 
    'TFT5_Item_RabadonsDeathcapRadiant': '라바돈의 초월한 죽음모자',
    'TFT5_Item_RedemptionRadiant': '면죄', 
    'TFT5_Item_RapidFirecannonRadiant': '고속 광자포',
    'TFT5_Item_ThiefsGlovesRadiant': '장난꾸러기의 장갑',
    'TFT5_Item_BrambleVestRadiant': '장미가시 조끼',
    'TFT5_Item_RunaansHurricaneRadiant': '루난의 폭풍', 
    'TFT5_Item_ShroudOfStillnessRadiant': '경외의 장막',
    'TFT5_Item_SpearOfShojinRadiant': '히라나의 창', 
    'TFT5_Item_StatikkShivRadiant': '스태틱의 호의',
    'TFT5_Item_SunfireCapeRadiant': '태양빛 망토',
    'TFT5_Item_TitansResolveRadiant': '거인의 맹세',
    'TFT5_Item_ArchangelsStaffRadiant': '우르프 천사의 지팡이',
    'TFT5_Item_WarmogsArmorRadiant': '워모그의 자부심',
    'TFT5_Item_ZekesHeraldRadiant': '지크의 조화', 
    'TFT5_Item_InfinityEdgeRadiant': '천공의 대검',
    'TFT5_Item_ZzRotPortalRadiant': '즈롯 소환문', 
    'TFT7_Item_ShimmerscaleDeterminedInvestor': '결단력 있는 투자자',
    'TFT7_Item_ShimmerscaleDravensAxe': '드레이븐의 도끼', 
    'TFT7_Item_ShimmerscaleMogulsMail': '거물의 갑옷',
    'TFT7_Item_ShimmerscaleGamblersBlade': '도박꾼의 칼날',
    'TFT7_Item_ShimmerscaleHeartOfGold': '쓸데없이 큰 보석', 
    'TFT7_Item_ShimmerscaleGoldmancersStaff': '황금술사의 지팡이', 
    'TFT7_Item_ShimmerscaleDiamondHands': '다이아몬드 손',
    'TFT8_Item_AnimaSquadEmblemItem': '동물특공대 상징',
    'TFT8_Item_CivilianEmblemItem': '민간인 상징', 
    'TFT8_Item_StarGuardianEmblemItem': '별 수호자 상징',
    'TFT8_Item_InterPolarisEmblemItem': '레이저단 상징', 
    'TFT8_Item_OxForceEmblemItem': '황소부대 상징', 
    'TFT8_Item_UndergroundTheEmblemItem': '지하세계 상징',
    'TFT8_Item_GenAEEmblemItem': '기계유망주 상징', 
    'TFT8_Item_ADMINEmblemItem': '자동방어체계 문장',
    'TFT8_Item_MascotEmblemItem': '마스코트 상징',
    'TFT8_Item_DefenderEmblemItem': '엄호대 상징',
    'TFT8_Item_ReconEmblemItem': '정찰단 상징',
    'TFT8_Item_RenegadeEmblemItem': '무법자 상징',
    'TFT8_Item_BrawlerEmblemItem': '싸움꾼 상징', 
    'TFT8_Item_HackerEmblemItem': '해커 상징', 
    'TFT8_Item_DuelistEmblemItem': '결투가 상징',
    'TFT8_Item_HeartEmblemItem': '선의 상징',
    'TFT8_Item_PranksterEmblemItem': '익살꾼 상징',
    'TFT8_Item_DeadeyeEmblemItem': '특등사수 상징',
    'TFT8_Item_GiantSlayer_GenAE': '과부하_ 오류 // 거인 학살자 ',
    'TFT8_Item_HandOfJustice_GenAE': '비결정적 정의의 손길',
    'TFT8_Item_RapidFireCannon_GenAE': '용수철이 든 고속 연사포',
    'TFT8_Item_Shojin_GenAE': '날뛰는 쇼진의 창',
    'TFT8_Item_Shroud_GenAE': '더 고요한 침묵의 장막',
    'TFT8_Item_Sunfire_GenAE': '과열된 태양불꽃 망토', 
    'TFT8_Item_Warmogs_GenAE': '유도집전형 워모그의 갑옷', 
    'TFT8_Item_ArsenalRedGun': '맹공',
    'TFT8_AdminEffect_Mana': '마나 @TFTUnitProperty.item:TFT8_Admin_ManaGained@ 획득', 
    'TFT8_Item_ArsenalBlueGun': '황혼파',
    'TFT8_AdminCause_OnCast': '', 
    'TFT8_Item_ArsenalPurpleGun': '속박의 월식', 
    'TFT8_AdminCause_CombatStart': '전투 시작: ', 
    'TFT8_AdminCause_EveryXAttacks': '', 
    'TFT8_AdminCause_EveryXSeconds': '', 
    'TFT8_AdminCause_HealthThreshold': '',
    'TFT8_AdminCause_OnEnemyDeath': '',
    'TFT8_AdminEffect_AttackSpeed': '공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득',
    'TFT8_AdminEffect_GainAP': '주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminEffect_Gold': '@TFTUnitProperty.item:TFT8_Admin_GoldChance@% 확률로 골드 획득',
    'TFT8_AdminEffect_Shield': '체력의 @TFTUnitProperty.item:TFT8_Admin_ShieldAmount@%만큼 피해를 흡수하는 보호막 획득',
    'TFT8_Item_ExoPrimeEmblemItem': '메카: 프라임 상징',
    'TFT8_Item_AceEmblemItem': '에이스 상징',
    'TFT_Assist_Gold_5': '5골드',
    'TFT_Assist_Gold_6': '6골드',
    'TFT_Assist_Gold_7': '7골드',
    'TFT_Assist_Gold_8': '8골드',
    'TFT_Assist_Gold_10': '10골드',
    'TFT_Assist_Gold_16': '16골드',
    'TFT8_AdminCause_AllyDeath': '',
    'TFT8_AdminEffect_GainAD': '공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득',
    'TFT8_AdminEffect_Heal': '체력 @TFTUnitProperty.item:TFT8_Admin_HealAmount@ 회복',
    'TFT8_AdminEffect_PermanentHealth': '최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득',
    'TFT8_AdminEffect_SingleTargetDamage': '자동방어체계 유닛의 현재 대상에게 고정 피해를 입히는 미사일 발사',
    'TFT_Assist_Gold_34': '34골드',
    'TFT_Assist_Gold_18': '18골드',
    'TFT_Assist_Gold_22': '22골드', 
    'TFT_Assist_Gold_54': '54골드',
    'TFT_Assist_Gold_12': '12골드',
    'TFT_Assist_Gold_20': '20골드',
    'TFT_Assist_Gold_24': '24골드',
    'TFT_Assist_Gold_36': '36골드',
    'TFT_Assist_Gold_76': '76골드',
    'TFT_Assist_Gold_30': '30골드',
    'TFT_Assist_Gold_25': '25골드',
    'TFT_Assist_Gold_40': '40골드',
    'TFT_Assist_Gold_100': '100골드',
    'TFT_Assist_Gold_26': '26골드',
    'TFT_Assist_Gold_126': '126골드',
    'TFT_Assist_Gold_44': '44골드',
    'TFT_Assist_Gold_64': '64골드',
    'TFT_Assist_Gold_154': '154골드',
    'TFT8_Item_ChannelerEmblemItem': '주문투척자 상징',
    'TFT_Random_5_Cost': '감옥 탈출!',
    'TFT_Random_Two_Star_4_Cost': '감옥 탈출!',
    'TFT8_Consumable_ExoPrime_PrimeMarker': '프라임 선택기',
    'TFT8_Item_AegisEmblemItem': '방패대 상징',
    'TFT8_AdminCauseEffect_AllyDeath_GainAP': '아군 사망 시 자동방어체계 유닛이 주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminCauseEffect_HealthThreshold_PermanentHealth': '체력이 40%일 때 자동방어체계 유닛이 최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득',
    'TFT8_AdminCauseEffect_OnCast_AttackSpeed': '스킬 사용 시 자동방어체계 유닛이 공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득',
    'TFT8_AdminCauseEffect_AllyDeath_GainMana': '아군 사망 시 자동방어체계 유닛이 마나 @TFTUnitProperty.trait:TFT8_Admin_ManaGained@ 획득',
    'TFT8_AdminCauseEffect_AllyDeath_Shield': '아군 자동방어체계 유닛 사망 시 최대 체력의 @TFTUnitProperty.item:TFT8_Admin_ShieldAmount@%만큼 피해를 흡수하는 보호막 획득',
    'TFT8_AdminCauseEffect_AllyDeath_AttackSpeed': '아군 사망 시 자동방어체계 유닛이 공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득',
    'TFT8_AdminCauseEffect_AllyDeath_Heal': '아군 사망 시 자동방어체계 유닛이 체력 @TFTUnitProperty.item:TFT8_Admin_HealAmount@ 회복',
    'TFT8_AdminCauseEffect_AllyDeath_GainAD': '아군 사망 시 자동방어체계 유닛이 공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득',
    'TFT8_AdminCauseEffect_AllyDeath_PermanentHealth': '아군 사망 시 자동방어체계 유닛이 최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득',
    'TFT8_AdminCauseEffect_OnCast_GainAP': '스킬 사용 시 자동방어체계 유닛이 주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminCauseEffect_OnCast_Mana': '스킬 사용 시 자동방어체계 유닛이 마나 @TFTUnitProperty.item:TFT8_Admin_ManaGained@ 획득',
    'TFT8_AdminCauseEffect_OnCast_Shield': '스킬 사용 시 자동방어체계 유닛이 체력의 @TFTUnitProperty.item:TFT8_Admin_ShieldAmount@%만큼 피해를 흡수하는 보호막 획득',
    'TFT8_AdminCauseEffect_OnCast_Heal': '스킬 사용 시 자동방어체계 유닛이 체력 @TFTUnitProperty.item:TFT8_Admin_HealAmount@ 회복',
    'TFT8_AdminCauseEffect_OnCast_GainAD': '스킬 사용 시 자동방어체계 유닛이 공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득',
    'TFT8_AdminCauseEffect_EveryXAttacks_GainAP': '3번째 기본 공격을 할 때마다 주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminCauseEffect_EveryXAttacks_Mana': '3번째 기본 공격을 할 때마다 마나 @TFTUnitProperty.item:TFT8_Admin_ManaGained@ 획득', 
    'TFT8_AdminCauseEffect_EveryXAttacks_Shield': '3번째 기본 공격을 할 때마다 체력의 @TFTUnitProperty.item:TFT8_Admin_ShieldAmount@%만큼 피해를 흡수하는 보호막 획득',
    'TFT8_AdminCauseEffect_EveryXAttacks_AttackSpeed': '3번째 기본 공격을 할 때마다 자동방어체계 유닛이 공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득',
    'TFT8_AdminCauseEffect_EveryXAttacks_Heal': '3번째 기본 공격을 할 때마다 체력 @TFTUnitProperty.item:TFT8_Admin_HealAmount@ 회복',
    'TFT8_AdminCauseEffect_EveryXAttacks_GainAD': '3번째 기본 공격을 할 때마다 공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득',
    'TFT8_AdminCauseEffect_EveryXAttacks_PermanentHealth': '3번째 기본 공격을 할 때마다 최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득',
    'TFT8_AdminCauseEffect_OnKill_GainAP': '처치 시 처치자가 주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminCauseEffect_OnKill_Mana': '처치 시 처치자가 마나 @TFTUnitProperty.item:TFT8_Admin_ManaGained@ 획득', 
    'TFT8_AdminCauseEffect_OnKill_Shield': '처치 시 처치자가 체력의 @TFTUnitProperty.item:TFT8_Admin_ShieldAmount@%만큼 피해를 흡수하는 보호막 획득', 
    'TFT8_AdminCauseEffect_OnKill_AttackSpeed': '처치 시 처치자가 공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득', 
    'TFT8_AdminCauseEffect_OnKill_Heal': '처치 시 처치자가 체력 @TFTUnitProperty.item:TFT8_Admin_HealAmount@ 회복',
    'TFT8_AdminCauseEffect_OnKill_GainAD': '처치 시 처치자가 공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득', 
    'TFT8_AdminCauseEffect_OnKill_PermanentHealth': '처치 시 처치자가 최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득', 
    'TFT8_AdminCauseEffect_HealthThreshold_GainAP': '체력이 40%일 때 자동방어체계 유닛이 주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminCauseEffect_HealthThreshold_Mana': '체력이 40%일 때 자동방어체계 유닛이 마나 @TFTUnitProperty.item:TFT8_Admin_ManaGained@ 획득',
    'TFT8_AdminCauseEffect_HealthThreshold_Shield': '체력이 40%일 때 자동방어체계 유닛이 체력의 @TFTUnitProperty.item:TFT8_Admin_ShieldAmount@%만큼 피해를 흡수하는 보호막 획득',
    'TFT8_AdminCauseEffect_HealthThreshold_AttackSpeed': '체력이 40%일 때 자동방어체계 유닛이 공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득',
    'TFT8_AdminCauseEffect_HealthThreshold_Heal': '체력이 40%일 때 자동방어체계 유닛이 체력 @TFTUnitProperty.item:TFT8_Admin_HealAmount@ 회복',
    'TFT8_AdminCauseEffect_HealthThreshold_GainAD': '체력이 40%일 때 자동방어체계 유닛이 공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득',
    'TFT8_AdminCauseEffect_CombatStart_GainAP': '전투 시작: 자동방어체계 유닛이 주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminCauseEffect_CombatStart_Mana': '전투 시작: 자동방어체계 유닛이 마나 @TFTUnitProperty.item:TFT8_Admin_ManaGained@ 획득',
    'TFT8_AdminCauseEffect_CombatStart_Shield': '전투 시작: 자동방어체계 유닛이 체력의 @TFTUnitProperty.item:TFT8_Admin_ShieldAmount@%만큼 피해를 흡수하는 보호막 획득',
    'TFT8_AdminCauseEffect_CombatStart_AttackSpeed': '전투 시작: 자동방어체계 유닛이 공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득',
    'TFT8_AdminCauseEffect_CombatStart_GainAD': '전투 시작: 자동방어체계 유닛이 공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득',
    'TFT8_AdminCauseEffect_CombatStart_PermanentHealth': '전투 시작: 자동방어체계 유닛이 최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득',
    'TFT8_AdminCauseEffect_EveryXSeconds_GainAP': '5초마다 자동방어체계 유닛이 주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminCauseEffect_EveryXSeconds_Mana': '5초마다 자동방어체계 유닛이 마나 @TFTUnitProperty.item:TFT8_Admin_ManaGained@ 획득',
    'TFT8_AdminCauseEffect_EveryXSeconds_Shield': '5초마다 자동방어체계 유닛이 체력의 @TFTUnitProperty.item:TFT8_Admin_ShieldAmount@%만큼 피해를 흡수하는 보호막 획득',
    'TFT8_AdminCauseEffect_EveryXSeconds_AttackSpeed': '5초마다 자동방어체계 유닛이 공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득',
    'TFT8_AdminCauseEffect_EveryXSeconds_Heal': '5초마다 자동방어체계 유닛이 체력 @TFTUnitProperty.item:TFT8_Admin_HealAmount@ 회복',
    'TFT8_AdminCauseEffect_EveryXSeconds_GainAD': '5초마다 자동방어체계 유닛이 공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득',
    'TFT8_AdminCauseEffect_EveryXSeconds_PermanentHealth': '5초마다 자동방어체계 유닛이 최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득',
    'TFT8_Item_Bloodthirster_GenAE': '톱날 피바라기',
    'TFT8_AdminCauseEffect_OnCast_PermanentHealth': '스킬 사용 시 자동방어체계 유닛이 최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득',
    'TFT8_Item_IonicSpark_GenAE': '자화 이온 충격기', 'TFT8_AdminCause_CombatStartTeam': '전투 시작: ',
    'TFT8_AdminCause_EveryXSecondsTeam': '전투 시작: ',
    'TFT8_AdminCauseEffect_CombatStartTeam_AttackSpeed': '전투 시작: 아군이 공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득',
    'TFT8_AdminCauseEffect_CombatStartTeam_GainAD': '전투 시작: 아군이 공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득',
    'TFT8_AdminCauseEffect_CombatStartTeam_GainAP': '전투 시작: 아군이 주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminCauseEffect_CombatStartTeam_Mana': '전투 시작: 아군이 마나 @TFTUnitProperty.item:TFT8_Admin_ManaGained@ 획득',
    'TFT8_AdminCauseEffect_CombatStartTeam_PermHP': '전투 시작: 아군이 최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득',
    'TFT8_AdminCauseEffect_CombatStartTeam_Shield': '전투 시작: 아군이 체력의 @TFTUnitProperty.item:TFT8_Admin_ShieldAmount@%만큼 피해를 흡수하는 보호막 획득',
    'TFT8_AdminCauseEffect_EveryXSecsTeam_AttackSpeed': '5초마다 아군이 공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득',
    'TFT8_AdminCauseEffect_EveryXSecsTeam_GainAD': '5초마다 아군이 공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득',
    'TFT8_AdminCauseEffect_EveryXSecsTeam_GainAP': '5초마다 아군이 주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminCauseEffect_EveryXSecsTeam_Heal': '5초마다 아군이 체력 @TFTUnitProperty.item:TFT8_Admin_HealAmount@ 회복',
    'TFT8_AdminCauseEffect_EveryXSecsTeam_Mana': '5초마다 아군이 마나 @TFTUnitProperty.item:TFT8_Admin_ManaGained@ 획득',
    'TFT8_AdminCauseEffect_EveryXSecsTeam_PermHP': '5초마다 아군이 최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득',
    'TFT_Item_GrantCompletedAnvil': '완성 아이템 열쇠',
    'TFT_Item_GrantComponentAnvil': '조합 아이템 열쇠',
    'TFT_Item_GrantTomeOfTraits': '특성의 고서', 
    'TFT_Item_GrantCompletedItem1': '완성 아이템 1개',
    'TFT_Item_GrantCompletedItem2': '완성 아이템 @ItemsToGive@개',
    'TFT_Item_GrantCompletedItem3': '완성 아이템 @ItemsToGive@개',
    'TFT_Item_GrantComponent1': '조합 아이템 1개',
    'TFT_Item_GrantComponent2': '조합 아이템 @ItemsToGive@개',
    'TFT_Item_GrantComponent3': '조합 아이템 @ItemsToGive@개',
    'TFT_Item_GrantComponent4': '조합 아이템 @ItemsToGive@개',
    'TFT_Item_GrantComponent5': '조합 아이템 @ItemsToGive@개',
    'TFT_Item_GrantComponent6': '조합 아이템 @ItemsToGive@개',
    'TFT_Item_GrantComponent7': '조합 아이템 @ItemsToGive@개',
    'TFT_Item_GrantComponent8': '조합 아이템 @ItemsToGive@개',
    'TFT_Item_GrantComponent9': '조합 아이템 @ItemsToGive@개',
    'TFT_Item_GrantOrbs1': '전리품 구 1개',
    'TFT_Item_GrantOrnnAnvil': '오른의 아이템 모루'
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
    'TFT6_Augment_ForceOfNature': '신병',
    'TFT6_Augment_FirstAidKit': '응급처치 키트 I',
    'TFT6_Augment_MaxLevel10': '레벨 업!', 
    'TFT6_Augment_ItemGrabBag1': '아이템 꾸러미 I', 
    'TFT6_Augment_ItemGrabBag2': '아이템 꾸러미 II', 
    'TFT6_Augment_Windfall': '뜻밖의 횡재',
    'TFT6_Augment_GrandGambler': '큰손',
    'TFT6_Augment_CalculatedLoss': '계산된 패배', 
    'TFT6_Augment_SalvageBin': '재활용 쓰레기통',
    'TFT6_Augment_SlowAndSteady': '진보의 행진',
    'TFT6_Augment_PortableForge': '휴대용 대장간', 
    'TFT6_Augment_HighEndShopping': '품격있는 쇼핑', 
    'TFT6_Augment_Diversify1': '단결된 의지 I', 
    'TFT6_Augment_Diversify2': '단결된 의지 II',
    'TFT6_Augment_Diversify3': '단결된 의지 III',
    'TFT6_Augment_BandOfThieves2': '도둑 무리 II',
    'TFT6_Augment_Featherweights1': '경량급 I',
    'TFT6_Augment_Featherweights2': '경량급 II', 
    'TFT6_Augment_Featherweights3': '경량급 III',
    'TFT6_Augment_HyperRoll': '수완가',
    'TFT6_Augment_MetabolicAccelerator': '대사 촉진제',
    'TFT6_Augment_MakeshiftArmor1': '임시변통 방어구 I',
    'TFT6_Augment_MakeshiftArmor2': '임시변통 방어구 II',
    'TFT6_Augment_Ascension': '초월', 
    'TFT6_Augment_BinaryAirdrop': '이중 공중 보급',
    'TFT6_Augment_ClearMind': '맑은 정신',
    'TFT6_Augment_ThriftShop': '현명한 소비', 
    'TFT6_Augment_Recombobulator': '대격변 생성기', 
    'TFT6_Augment_RadiantRelics': '찬란한 유물',
    'TFT6_Augment_JeweledLotus': '보석 연꽃',
    'TFT6_Augment_VerdantVeil': '신록의 장막',
    'TFT6_Augment_TinyTitans': '꼬마 거인', 
    'TFT6_Augment_ComponentGrabBag': '재료 꾸러미', 
    'TFT6_Augment_Twins2': '문제가 두 배 II', 
    'TFT6_Augment_Twins3': '문제가 두 배 III',
    'TFT6_Augment_FuturePeepers2': '예견 II',
    'TFT6_Augment_TrueTwos': '곱빼기',
    'TFT6_Augment_TriForce1': '3에 깃든 힘 I',
    'TFT6_Augment_TriForce2': '3에 깃든 힘 II',
    'TFT6_Augment_TriForce3': '3에 깃든 힘 III',
    'TFT6_Augment_TheGoldenEgg': '황금 알', 
    'TFT7_Augment_ThinkFast': '빠른 판단',
    'TFT7_Augment_Bloodlust1': '전투 훈련',
    'TFT7_Augment_SacrificialPact': '잔혹한 계약',
    'TFT7_Augment_PandorasBench': '판도라의 대기석',
    'TFT7_Augment_AxiomArc2': '원칙의 원형낫 II',
    'TFT7_Augment_ClutteredMind': '어수선한 마음',
    'TFT6_Augment_TradeSector': '교환의 장',
    'TFT6_Augment_Distancing': '추방자 I', 
    'TFT6_Augment_Distancing2': '추방자 II',
    'TFT6_Augment_ThreesCompany': '삼총사',
    'TFT7_Augment_UrfsGrabBag2': '우르프의 꾸러미 II',
    'TFT7_Augment_LivingForge': '간이 대장간',
    'TFT7_Augment_AFK': '자리 비움',
    'TFT7_Augment_BandOfThieves1': '도둑 무리 I',
    'TFT7_Augment_LategameSpecialist': '후반 전문가',
    'TFT7_Augment_Preparation': '준비 I',
    'TFT7_Augment_BigFriend': '커다란 친구 I',
    'TFT7_Augment_LastStand': '최후의 저항',
    'TFT6_Augment_TargetDummies': '허수아비 전선',
    'TFT7_Augment_CursedCrown': '저주받은 왕관',
    'TFT6_Augment_CyberneticImplants1': '사이버네틱 이식술 I',
    'TFT6_Augment_CelestialBlessing1': '천상의 축복 I',
    'TFT6_Augment_SecondWind1': '재생의 바람 I',
    'TFT6_Augment_CyberneticShell1': '사이버네틱 외피 I',
    'TFT6_Augment_CyberneticUplink1': '사이버네틱 통신 I',
    'TFT6_Augment_CyberneticImplants3': '사이버네틱 이식술 III',
    'TFT6_Augment_CyberneticShell3': '사이버네틱 외피 III',
    'TFT6_Augment_CyberneticUplink3': '사이버네틱 통신 III',
    'TFT6_Augment_RichGetRicher': '부익부', 
    'TFT6_Augment_RichGetRicherPlus': '부익부+',
    'TFT6_Augment_Electrocharge1': '고전압 I', 
    'TFT6_Augment_LudensEcho1': '루덴의 메아리 I', 
    'TFT6_Augment_CelestialBlessing2': '천상의 축복 II', 
    'TFT6_Augment_CelestialBlessing3': '천상의 축복 III',
    'TFT6_Augment_SecondWind2': '재생의 바람 II',
    'TFT6_Augment_ThrillOfTheHunt1': '사냥의 전율 I', 
    'TFT6_Augment_ThrillOfTheHunt2': '사냥의 전율 II',
    'TFT6_Augment_LudensEcho2': '루덴의 메아리 II',
    'TFT6_Augment_LudensEcho3': '루덴의 메아리 III', 
    'TFT6_Augment_Electrocharge2': '고전압 II',
    'TFT6_Augment_Electrocharge3': '고전압 III', 
    'TFT6_Augment_CyberneticImplants2': '사이버네틱 이식술 II',
    'TFT6_Augment_CyberneticShell2': '사이버네틱 외피 II',
    'TFT6_Augment_CyberneticUplink2': '사이버네틱 통신 II',
    'TFT6_Augment_SunfireBoard': '태양불꽃판',
    'TFT6_Augment_WindfallPlus': '뜻밖의 횡재+',
    'TFT6_Augment_WindfallPlusPlus': '뜻밖의 횡재++',
    'TFT7_Augment_FirstAidKit2': '응급처치 키트 II',
    'TFT7_Augment_BigFriend2': '커다란 친구 II', 
    'TFT7_Augment_Preparation2': '준비 II', 
    'TFT7_Augment_Preparation3': '준비 III',
    'TFT6_Augment_TradeSectorPlus': '교환의 장+', 
    'TFT8_Augment_ThreatMaxHealth': '위협 레벨: 최대',
    'TFT8_Augment_AceEmblem': '에이스 문장',
    'TFT8_Augment_AceEmblem2': '에이스 왕관', 
    'TFT8_Augment_ADMINEmblem': '자동방어체계 문장',
    'TFT8_Augment_ADMINEmblem2': '자동방어체계 왕관',
    'TFT8_Augment_AnimaSquadEmblem': '동물특공대 문장', 
    'TFT8_Augment_AnimaSquadEmblem2': '동물특공대 왕관',
    'TFT8_Augment_BrawlerEmblem': '싸움꾼 문장', 
    'TFT8_Augment_BrawlerEmblem2': '싸움꾼 왕관',
    'TFT8_Augment_ChannelerEmblem': '주문투척자 문장',
    'TFT8_Augment_ChannelerEmblem2': '주문투척자 왕관',
    'TFT8_Augment_CivilianEmblem': '민간인 문장',
    'TFT8_Augment_CivilianEmblem2': '민간인 왕관',
    'TFT8_Augment_DeadeyeEmblem': '특등사수 문장',
    'TFT8_Augment_DeadeyeEmblem2': '특등사수 왕관',
    'TFT8_Augment_DefenderEmblem': '엄호대 문장',
    'TFT8_Augment_DefenderEmblem2': '엄호대 왕관',
    'TFT8_Augment_DuelistEmblem': '결투가 문장',
    'TFT8_Augment_DuelistEmblem2': '결투가 왕관',
    'TFT8_Augment_ExoPrimeEmblem': '메카: 프라임 문장',
    'TFT8_Augment_ExoPrimeEmblem2': '메카: 프라임 왕관',
    'TFT8_Augment_GenAETrait2': '기계유망주 영혼',
    'TFT8_Augment_AegisEmblem': '방패대 문장',
    'TFT8_Augment_AegisEmblem2': '방패대 왕관', 
    'TFT8_Augment_HackerEmblem': '해커 문장', 
    'TFT8_Augment_HackerEmblem2': '해커 왕관', 
    'TFT8_Augment_HeartEmblem': '선의 문장', 
    'TFT8_Augment_HeartEmblem2': '선의 왕관',
    'TFT8_Augment_InterPolarisEmblem': '레이저단 문장',
    'TFT8_Augment_InterPolarisEmblem2': '레이저단 왕관',
    'TFT8_Augment_MascotEmblem': '마스코트 문장',
    'TFT8_Augment_MascotEmblem2': '마스코트 왕관',
    'TFT8_Augment_OxForceEmblem': '황소부대 문장',
    'TFT8_Augment_OxForceEmblem2': '황소부대 왕관',
    'TFT8_Augment_PranksterEmblem': '익살꾼 문장', 
    'TFT8_Augment_PranksterEmblem2': '익살꾼 왕관',
    'TFT8_Augment_ReconEmblem': '정찰단 문장', 
    'TFT8_Augment_ReconEmblem2': '정찰단 왕관', 
    'TFT8_Augment_RenegadeEmblem': '무법자 문장', 
    'TFT8_Augment_RenegadeEmblem2': '무법자 왕관',
    'TFT8_Augment_StarGuardianEmblem': '별 수호자 문장',
    'TFT8_Augment_StarGuardianEmblem2': '별 수호자 왕관',
    'TFT8_Augment_UndergroundTheTrait2': '지하세계 영혼', 
    'TFT6_Augment_WoodlandCharm': '숲의 부적', 
    'TFT7_Augment_LuckyGloves': '행운의 장갑', 
    'TFT7_Augment_ScopedWeapons1': '조준경 부착 I',
    'TFT6_Augment_Battlemage1': '전투 마법사 I',
    'TFT6_Augment_Battlemage2': '전투 마법사 II',
    'TFT6_Augment_Battlemage3': '전투 마법사 III',
    'TFT6_Augment_MeleeStarBlade1': '나이프의 날 I',
    'TFT6_Augment_MeleeStarBlade2': '나이프의 날 II',
    'TFT6_Augment_MeleeStarBlade3': '나이프의 날 III',
    'TFT7_Augment_BirthdayPresents': '생일 선물', 
    'TFT7_Augment_Consistency': '일관성', 
    'TFT8_Augment_AnimaSquadTrait': '동물특공대 심장',
    'TFT8_Augment_StarGuardianTrait': '별 수호자 심장',
    'TFT8_Augment_InterPolarisTrait': '레이저단 심장',
    'TFT8_Augment_OxForceTrait': '황소부대 심장',
    'TFT8_Augment_GenAETrait': '기계유망주 심장',
    'TFT8_Augment_MascotTrait': '마스코트 심장',
    'TFT8_Augment_DefenderTrait': '엄호대 심장', 
    'TFT8_Augment_ChannelerTrait': '주문투척자 심장', 
    'TFT8_Augment_BrawlerTrait': '싸움꾼 심장', 
    'TFT8_Augment_DuelistTrait': '결투가 심장', 
    'TFT8_Augment_HeartTrait': '선의 심장',
    'TFT8_Augment_DeadeyeTrait': '특등사수 심장', 
    'TFT8_Augment_ReconTrait': '정찰단 심장',
    'TFT8_Augment_RenegadeTrait': '무법자 심장',
    'TFT8_Augment_UndergroundTheTrait': '지하세계 심장',
    'TFT8_Augment_SupersTrait': '우세 심장', 
    'TFT8_Augment_SupersTrait2': '우세 영혼',
    'TFT8_Augment_ADMINTrait': '자동방어체계 심장', 
    'TFT8_Augment_HackerTrait': '해커 심장', 
    'TFT6_Augment_TomeOfTraits1': '고대의 기록 보관소 I',
    'TFT7_Augment_TomeOfTraits2': '고대의 기록 보관소 II', 
    'TFT6_Augment_Traitless2': '다른 태생 II', 
    'TFT6_Augment_Traitless3': '다른 태생 III',
    'TFT6_Augment_FuturePeepers': '예견 I',
    'TFT6_Augment_GachaAddict': '황금 티켓',
    'TFT8_Augment_BelVethVoidmother': '공허 어미',
    'TFT8_Augment_AurelionSolImpact': '충격 속도',
    'TFT8_Augment_ChoGathMR': '우주의 방어막',
    'TFT8_Augment_RammusArmor': '중무장 아르마딜로',
    'TFT8_Augment_VelkozFrostburn': '동상',
    'TFT8_Augment_ZacSupersize': '거대화', 
    'TFT8_Augment_SonaExile': '전력망', 
    'TFT8_Augment_SonaSupport': '암류',
    'TFT8_Augment_AlistarAoEPulverizer': '강타!',
    'TFT8_Augment_JaxASCarry': '가차없는 맹공',
    'TFT8_Augment_SennaASCarry': '면죄', 
    'TFT8_Augment_NilahReflection': '나눔의 미덕',
    'TFT8_Augment_ZoeDoubleTrouble': '이중 방울',
    'TFT8_Augment_SennaSupport': '레이저단 진형',
    'TFT8_Augment_AlistarBeefUp': '괴수',
    'TFT8_Augment_RivenReverberation': '반향',
    'TFT8_Augment_AnnieCarry': '반사 방패', 
    'TFT8_Augment_AnnieSupport': '불타는 영혼',
    'TFT8_Augment_CamilleCarry': '적응형 방어 체계',
    'TFT8_Augment_LeeSinSupport': '고양',
    'TFT8_Augment_RellSupport': '변화의 철마술',
    'TFT8_Augment_YuumiSupport': '슈우우웅!',
    'TFT8_Augment_ViSupport': '권투 교습',
    'TFT8_Augment_SivirSupport': '끝없는 피자',
    'TFT8_Augment_KaisaStarCrossed': '엇갈린 별', 
    'TFT8_Augment_YasuoCarry': '흡수의 바람', 
    'TFT8_Augment_LeBlancGlitch': '조준 보정', 
    'TFT8_Augment_FioraCarry': '전방의 검사', 
    'TFT8_Augment_EzrealSupport': '도굴꾼의 전리품',
    'TFT8_Augment_JinxCarry': '신난다!',
    'TFT8_Augment_MalphiteCarry': '견고',
    'TFT8_Augment_NasusCarry': '쌓고 또 쌓고',
    'TFT8_Augment_DravenCarry': '드레이븐의 리그',
    'TFT8_Augment_KaisaCarry': '다중 사격', 
    'TFT8_Augment_GalioCarry': '정의의 주먹', 
    'TFT8_Augment_GalioSupport': '안전제일',
    'TFT8_Augment_AurelionSolCarry': '대멸종',
    'TFT8_Augment_JaxSupport': '회피',
    'TFT8_Augment_LuxCarry': '눈부신 특이점',
    'TFT8_Augment_PoppyCarry': '더 크고 튼튼한 방패',
    'TFT8_Augment_ApheliosSupport': '발포 준비 완료',
    'TFT8_Augment_LuxSupport': '빛의 방어막',
    'TFT8_Augment_GangplankSupport': '수금', 
    'TFT8_Augment_SylasCarry': '국왕시해자', 
    'TFT8_Augment_SylasSupport': '페트리사이트 사슬',
    'TFT8_Augment_SettCarry': '펀치 프로토콜',
    'TFT8_Augment_KayleCarry': '거룩한 승천', 
    'TFT8_Augment_KayleSupport': '정의로운 사거리',
    'TFT8_Augment_EkkoSupport': '시공간 붕괴', 
    'TFT8_Augment_MordekaiserCarry': '헤비하지 않은 메탈',
    'TFT8_Augment_VelkozSupport': '얼어붙은 땅',
    'TFT8_Augment_SettSupport': '재생형 보호막', 
    'TFT8_Augment_TalonCarry': '검의 군주',
    'TFT8_Augment_MissFortuneCarry': '토끼 용병',
    'TFT8_Augment_ChoGathCarry': '에너지 공허', 
    'TFT8_Augment_SyndraSupport': '예비전력 강화',
    'TFT8_Augment_RammusCarry': '가시박힌 껍질', 
    'TFT8_Augment_LeonaCarry': '완벽한 흑점 폭발', 
    'TFT8_Augment_NunuSupport': '퍼지는 웃음', 
    'TFT8_Augment_FiddlesticksCarry': '끔찍한 기억', 
    'TFT8_Augment_UrgotCarry': '반짝반짝', 
    'TFT8_Augment_JannaSupport': '과장된 보도',
    'TFT8_Augment_SamiraCarry': '스타일과 재능', 
    'TFT8_Augment_TaliyahSupport': '돌처럼 단단하게',
    'TFT8_Augment_ZedSupport': '약자 멸시', 
    'TFT8_Augment_BlitzcrankCarry': '동적 방어', 
    'TFT8_Augment_UrgotSupport': '밀물',
    'TFT8_Augment_BlitzcrankSupport': '로켓 손',
    'TFT8_Augment_MordekaiserSupport': '말살', 
    'TFT8_Augment_ApheliosCarry': '철갑탄', 
    'TFT8_Augment_LuluSupport': '성장 촉진', 
    'TFT8_Augment_LeonaSupport': '절정의 일식',
    'TFT8_Augment_SejuaniCarry': '빙하 감옥',
    'TFT8_Augment_SyndraCarry': '압도적인 힘',
    'TFT8_Augment_WukongSupport': '재충전',
    'TFT8_Augment_AsheCarry': '레이저단 집중',
    'TFT8_Augment_AsheSupport': '레이저단 몰입',
    'TFT8_Augment_NilahSupport': '승리의 장막',
    'TFT8_Augment_VayneSupport': '한밤의 서곡', 
    'TFT8_Augment_RivenSupport': '금의환향',
    'TFT8_Augment_ZoeSupport': '한숨 잘 시간',
    'TFT8_Augment_LeBlancSupport': '거울 환영', 
    'TFT8_Augment_LeeSinCarry': '정화의 방호', 
    'TFT8_Augment_YuumiCarry': '포식자의 정확성',
    'TFT8_Augment_FiddlesticksSupport': '완전한 타락',
    'TFT8_Augment_PoppySupport': '굳건한 태세',
    'TFT8_Augment_JannaCarry': '신속한 보도',
    'TFT8_Augment_RenegadePartners': '공범',
    'TFT8_Augment_TaliyahCarry': '바위술사',
    'TFT8_Augment_ZedCarry': '그림자술',
    'TFT8_Augment_SivirCarry': '배달팁',
    'TFT8_Augment_RenektonCarry': '분노의 지배',
    'TFT8_Augment_ViCarry': '무자비한 힘', 
    'TFT8_Augment_RenektonSupport': '양떼 도륙', 
    'TFT8_Augment_RellCarry': '진형 유지', 
    'TFT8_Augment_FioraSupport': '황소의 활력', 
    'TFT8_Augment_DravenSupport': '무자비한 칼날', 
    'TFT8_Augment_YasuoSupport': '추방자의 기백', 
    'TFT8_Augment_NasusSupport': '영혼의 포식자', 
    'TFT8_Augment_SorakaSupport': '융화', 
    'TFT8_Augment_LuluCarry': '급속 성장',
    'TFT8_Augment_SorakaCarry': '업그레이드: 광란',
    'TFT8_Augment_VayneCarry': '확산 사격', 
    'TFT8_Augment_MalphiteSupport': '수호자 영혼',
    'TFT8_Augment_BelVethCarry': '피의 복수',
    'TFT8_Augment_EkkoCarry': '공진',
    'TFT8_Augment_GangplankCarry': '불타는 도탄',
    'TFT8_Augment_JinxSupport': '전부 터져라!',
    'TFT8_Augment_MissFortuneSupport': '총알은 비를 타고', 
    'TFT8_Augment_CamilleSupport': '마법공학 응징',
    'TFT8_Augment_WukongCarry': '회전격', 
    'TFT8_Augment_SejuaniSupport': '산산조각', 
    'TFT8_Augment_ZacSupport': '새총 발사',
    'TFT8_Augment_NunuCarry': '눈 굴러가요',
    'TFT8_Augment_ViegoCarry': '심장을 멈추는 자',
    'TFT8_Augment_SamiraSupport': '무모한 자',
    'TFT8_Augment_TalonSupport': '황소부대의 분노',
    'TFT8_Augment_EzrealCarry': '끓어오르는 주문의 힘'
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

